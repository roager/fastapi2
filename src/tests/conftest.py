import pytest
from tortoise.contrib.test import initializer, finalizer

@pytest.fixture(scope="module", autouse=True)
def initialize_db():
    # 1) Inicializa Tortoise en memoria
    initializer(
        modules=["src.models"],   # aquí indicas el path a tus modelos
        db_url="sqlite://:memory:",
    )
    yield
    # 2) Finaliza y limpia las conexiones
    finalizer()
