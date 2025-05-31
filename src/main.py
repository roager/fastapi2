"""
src/main.py

Punto de entrada de la aplicación FastAPI.

Este módulo configura:
  1. La instancia de FastAPI con metadata y rutas de documentación.
  2. El registro de Tortoise ORM para la conexión a la base de datos.
  3. La inclusión de routers modulares (e.g., users).
  4. Endpoints globales (e.g., ruta raíz).

Variables de configuración:
  - APP_ENV (str): Entorno de ejecución ('development', 'production', etc.).
  - PORT (int): Puerto en el que corre la aplicación.
  - DATABASE_URL (str): Cadena de conexión a la base de datos (SQLite, Postgres, etc.).
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from src.config import DATABASE_URL, APP_ENV, PORT
from src.controllers.user_controller import router as user_router


# 1. Instancia FastAPI
# ---------------------
# - title: Título de la API en la documentación OpenAPI/Swagger.
# - version: Versión de la API.
# - description: Descripción general (opcional).
# - docs_url: Ruta para Swagger UI. Solo activa en desarrollo.
app = FastAPI(
    title="My FastAPI App",
    version="0.1.0",
    description="API de ejemplo con FastAPI, Tortoise ORM y modularidad por capas.",
    openapi_url="/openapi.json",
    docs_url="/docs" if APP_ENV == "development" else None,
)


# 2. Incluir routers modulares
# -----------------------------
# Agrupa rutas relacionadas bajo un mismo prefijo y tags.
# En main.py no definimos lógica; solo montamos controladores.
app.include_router(
    user_router,
    prefix="/users",      # Ruta base para todas las operaciones de usuario
    tags=["users"],        # Sección en Swagger UI
)


# 3. Configuración de Tortoise ORM
# --------------------------------
# register_tortoise:
# - app: instancia FastAPI para enganchar eventos de arranque/shutdown.
# - db_url: cadena de conexión, p.ej. sqlite://db.sqlite3 o postgres://...
# - modules: diccionario alias->lista de módulos donde están los modelos.
# - generate_schemas: si True, crea tablas automáticamente al arrancar (útil en dev).
# - add_exception_handlers: registra manejadores de excepción para errores de BD.
register_tortoise(
    app=app,
    db_url=DATABASE_URL,
    modules={"models": ["src.models"]},  # Alias 'models' para User, etc.
    generate_schemas=True,
    add_exception_handlers=True,
)


# 4. Endpoint global: Ruta raíz
# -----------------------------
@app.get(
    "/",
    summary="Ruta raíz",
    response_description="Mensaje de bienvenida al consumidor de la API",
    status_code=200,
)
async def root():
    """
    root

    Endpoint que devuelve un mensaje de confirmación de que la API está levantada.

    Returns:
        dict: Mensaje de bienvenida.
    """
    return {"message": "¡Hola, mundo!"}



