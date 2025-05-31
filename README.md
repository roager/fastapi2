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
   git clone https://github.com/jonaths/fastapi_starter

2. Instala dependencias con Poetry y crea un entorno virtual:

   ```bash
   poetry install

3. Configura variables de entorno

   ```bash
   cp .env.example .env
   
4. Editar .env según sea necesario. Por ejemplo. 
   ```
   # Entorno de ejecución: development o production
   APP_ENV=development
   
   # Puerto en el que correrá la aplicación (solo si corres local)
   PORT=8000
   
   # URL de conexión a la base de datos
   # Ejemplo para SQLite local:
   DATABASE_URL=sqlite://db.sqlite3
   
   # Ejemplo para Postgres (reemplaza los datos con tus credenciales):
   # DATABASE_URL=postgres://usuario:contraseña@localhost:5432/nombre_db
   ```
   
   Notas:

   - En desarrollo, basta con SQLite (sqlite://db.sqlite3).
   - En producción (Heroku o Docker), apunta a tu instancia de Postgres mediante DATABASE_URL.

## Levantar la aplicación en local

1. Levanta el servidor Uvicorn

   ```bash
   poetry run uvicorn src.main:app --reload
   ```
   
   - --reload activa recarga automática cuando detecta cambios en el código.
   - Por defecto, corre en http://127.0.0.1:8000 (o el puerto que definas en .env).

2. Verifica en el navegador o con curl
   
   - Abre tu navegador en http://127.0.0.1:8000/docs para acceder a la documentación interactiva Swagger UI.
   - Para probar rápidamente el endpoint raíz:
      ```bash
      curl http://127.0.0.1:8000/
      # Debe devolver: {"message":"¡Hola, mundo!"}

3. Prueba algunos endpoints de ejemplo:
   - Listar usuarios (GET)
   ```bash
   curl http://127.0.0.1:8000/users/
   ```
   - Crear usuario (POST):

bash
Copy
Edit

