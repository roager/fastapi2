# FastAPI App Starter

Proyecto base para una API construida con FastAPI, Tortoise ORM y Poetry.  
Incluye:

- Estructura modular (src/)
- FastAPI como servidor ASGI
- Tortoise ORM para conexión asíncrona a base de datos (SQLite/Postgres)
- Validación de datos con Pydantic
- Gestión de variables de entorno con Python-Decouple
- Esqueleto de tests con pytest
- Listo para desplegar en Heroku (Procfile, runtime.txt)

---

## Requisitos previos

1. **Python 3.10+** instalado (ver [`runtime.txt`](runtime.txt) para versión exacta).  
2. **Git** (para clonar el repositorio).  
3. **Poetry** (gestor de dependencias y entorno virtual).  
   - Si no lo tienes, instala siguiendo [la guía oficial](https://python-poetry.org/docs/#installation).

Opcionales (si usarás Postgres en lugar de SQLite):

- Un servidor de **PostgreSQL** en marcha (local o remoto).
- El comando `psql` en tu PATH (para validar conexión, backups, etc.).

---

## Configurar el proyecto

1. **Clona** este repositorio a tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/my-fastapi-app.git
   cd my-fastapi-app