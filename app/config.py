import os 
from dotenv import load_dotenv

load_dotenv()

class config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    # Configuracon de la BD
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )
    SQLARCHEY_TRACK_MODIFICATIONS = False