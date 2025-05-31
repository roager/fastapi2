"""
src/models.py

Definición del modelo User usando Tortoise ORM.

Este módulo define:
- Clase User: representa la entidad de usuario en la base de datos.
- Campos con tipos, restricciones y descripciones para validar y documentar.
"""

from tortoise import fields, models


class User(models.Model):
    """
    Modelo User para interacción con la tabla 'user' en la base de datos.

    Atributos:
        id (IntField): Clave primaria autoincremental.
        name (CharField): Nombre completo del usuario. Máximo 50 caracteres.
        email (CharField): Correo electrónico único. Máximo 100 caracteres.

    Métodos:
        __str__: Representación en cadena (útil para logs y debugging).
    """

    id = fields.IntField(
        pk=True,
        description="Clave primaria única para cada usuario"
    )
    name = fields.CharField(
        max_length=50,
        description="Nombre completo del usuario, hasta 50 caracteres"
    )
    email = fields.CharField(
        max_length=100,
        unique=True,
        description="Correo electrónico único del usuario, hasta 100 caracteres"
    )

    class Meta:
        """
        Opciones de configuración del modelo.

        - table: Nombre de la tabla en la base de datos.
        - ordering: Orden por defecto al recuperar instancias.
        """
        table = "users"
        ordering = ["name"]

    def __str__(self) -> str:
        """
        Retorna una cadena legible con el nombre del usuario.

        Returns:
            str: Nombre del usuario.

        Ejemplo:
            >>> str(user)
            'Ana Pérez'
        """
        return self.name
