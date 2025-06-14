import os
import sys

# 1) Calcular el directorio src/
HERE = os.path.dirname(__file__)            # …/src/api
SRC_ROOT = os.path.dirname(HERE)            # …/src

# 2) Añádir al path para que Python encuentre main.py
sys.path.append(SRC_ROOT)

# 3) Importar aplicación FastAPI
from main import app
