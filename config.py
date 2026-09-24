import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


DB_HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
BACKUP_KEY_PUB_FILE = os.getenv("BACKUP_KEY_PUB_FILE")
TIME_ZONE = os.getenv("TIME_ZONE", "Europe/Moscow")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "backup-dessan")
S3_ENDPOINT_URL = os.getenv(
    "S3_ENDPOINT_URL",
    "https://storage.yandexcloud.net",
)
BACKUP_API_URL = os.getenv(
    "BACKUP_API_URL",
    "http://storyka.ru/web/database/backup",
)
MASTER_PASSWORD = os.getenv("MASTER_PASSWORD", "mobile")
ODOO_DATABASE_NAME = os.getenv("ODOO_DATABASE_NAME", "service_app")
ODOO_DATABASE_FILE_NAME = os.getenv("ODOO_DATABASE_FILE_NAME", "backup_service_app.zip")
DB_FILENAME = os.getenv("DB_FILENAME", "/tmp/backup_db.sql.gz.enc")
