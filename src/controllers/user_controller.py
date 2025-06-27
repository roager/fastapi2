"""
src/controllers/user_controller.py

Controlador (API Router) para operaciones CRUD de Usuarios.

Este módulo define:
- Un esquema de datos de entrada (Pydantic) para validar payloads JSON.
- Endpoints para listar y crear usuarios.
- Uso de la capa de servicio (UserService) para separar lógica de negocio.
"""

from fastapi import APIRouter, HTTPException, status

from src.config import logger
from src.services.user_service import UserService
from pydantic import BaseModel, EmailStr

# ------------------------------------------------------------------------------
# 1. Definición del router
# ------------------------------------------------------------------------------
# APIRouter permite modularizar las rutas y luego montarlas en el FastAPI app
router = APIRouter(
    tags=["users"],             # Etiquetas para agrupar en la documentación automática
    responses={404: {"description": "Not found"}},  # Respuestas genéricas
)


# ------------------------------------------------------------------------------
# 2. Esquema de entrada (DTO)
# ------------------------------------------------------------------------------
class UserIn(BaseModel):
    """
    UserIn: esquema de validación para datos de creación de usuario.

    Atributos:
        name (str): Nombre completo del usuario. No vacío.
        email (EmailStr): Correo electrónico válido.
    """
    name: str
    email: EmailStr


# ------------------------------------------------------------------------------
# 3. Endpoint: Listar todos los usuarios
# ------------------------------------------------------------------------------
@router.get(
    "/",
    summary="Listar usuarios",
    description="Obtiene la lista completa de usuarios registrados en la base de datos.",
    response_model=list[UserIn],   # Doc: indica que devuelve una lista de UserIn
    status_code=status.HTTP_200_OK
)
async def list_users():
    """
    list_users

    Llama a UserService.get_all() para recuperar todos los usuarios.

    Returns:
        list[UserIn]: Lista de usuarios (serializados automáticamente a JSON).
    """
    # Lógica:
    # - La capa de servicio abstrae el acceso a la base de datos.
    # - FastAPI transforma el resultado en JSON y aplica el modelo de respuesta.
    print("Hola...")
    try:
        return await UserService.get_all()
    except Exception as exception:
        print(exception)
        logger.exception(exception)

# ------------------------------------------------------------------------------
# 4. Endpoint: Crear un usuario
# ------------------------------------------------------------------------------
@router.post(
    "/",
    summary="Crear usuario",
    description="Crea un nuevo usuario con nombre y correo electrónico. "
                "Valida el payload y devuelve el usuario recién creado.",
    response_model=UserIn,        # Doc: el usuario creado
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"description": "Datos inválidos o usuario no pudo crearse"},
        422: {"description": "Error de validación de entrada (Pydantic)"}
    }
)
async def create_user(payload: UserIn):
    """
    create_user

    Parámetros:
        payload (UserIn): Objeto Pydantic con los campos 'name' y 'email'.

    Flujo:
    1. Valida automáticamente el JSON de entrada con Pydantic.
    2. Llama a UserService.create() para persistir en la base de datos.
    3. Si falla (e.g., email duplicado), lanza HTTPException(400).
    4. Devuelve el objeto User recién creado.

    Returns:
        UserIn: Datos del usuario creado.
    Raises:
        HTTPException: Código 400 si no se pudo crear.
    """
    # 1. Crear usuario en la capa de servicio
    user = await UserService.create(name=payload.name, email=payload.email)

    # 2. Validación de creación exitosa
    if user is None:
        # HTTPException detona una respuesta con código y mensaje custom
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se pudo crear el usuario"
        )

    # 3. Devolver objeto Pydantic serializado a JSON
    return user

@router.get("/group")
async def get_user_group(age: int):
    try:
        age_group = UserService.get_age_group(age)
        return {"age_group": age_group}
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )


