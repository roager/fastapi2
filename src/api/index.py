import os
import sys

# 1) Ubicaciones de carpeta
HERE     = os.path.dirname(__file__)        # …/src/api
SRC_DIR  = os.path.dirname(HERE)            # …/src
ROOT_DIR = os.path.dirname(SRC_DIR)
sys.path.insert(0, ROOT_DIR)

# 2) Importa la app (que ahora tendrá el middleware)
from src.main import app
