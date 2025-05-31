from decouple import config

APP_ENV = config("APP_ENV", default="production")
PORT = config("PORT", cast=int, default=8000)
DATABASE_URL = config("DATABASE_URL", default="sqlite://db.sqlite3")
