import os

# Variables de entorno (seguras)
DB_USER = os.environ.get('DB_USER', 'igrafic3_referidos')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'enerop2003')
DB_NAME = os.environ.get('DB_NAME', 'igrafic3_referidos')
DB_HOST = os.environ.get('DB_HOST', 'localhost')

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# CORS - Dominios permitidos
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "https://igrafic360.net",
    "https://www.igrafic360.net",
    "https://vitaesentia.com",
    "https://www.vitaesentia.com",
    "https://vitaesen-cp506.wordpresstemporal.com"
]