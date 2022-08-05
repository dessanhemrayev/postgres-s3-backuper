"""
Backup PostgreSQL database to Yandex Object Storage, that has S3 compatible
API.
"""
import datetime
import os
from pathlib import Path
import pytz

from termcolor import colored
import boto3


DB_HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
BACKUP_KEY_PUB_FILE = os.getenv("BACKUP_KEY_PUB_FILE")


DB_FILENAME = "/tmp/backup_db.sql.gz.enc"


MASTER_PASSWORD = 'mobile'
ODOO_DATABASE_NAME = 'service_app'
ODOO_DATABASE_FILE_NAME = 'backup_service_app' 
TIME_ZONE = os.getenv("TIME_ZONE", "Europe/Moscow")
S3_BUCKET_NAME = "YCOviGAVKowRNkBt9V6vAek5sSQ_xUaYabOhffGp"

def say_hello():
    print(colored("Hi! This tool will dump PostgreSQL database, compress \n"
        "and encode it, and then send to Yandex Object Storage.\n", "cyan"))


def get_now_datetime_str():
    now = datetime.datetime.now(pytz.timezone(TIME_ZONE))
    return now.strftime('%Y-%m-%d__%H-%M-%S')


def check_key_file_exists():
    if not Path(BACKUP_KEY_PUB_FILE).is_file():
        exit(
            f"\U00002757 Public encrypt key ({BACKUP_KEY_PUB_FILE}) "
            f"not found. If you have no key – you need to generate it. "
            f"You can find help here: "
            f"https://www.imagescape.com/blog/2015/12/18/encrypted-postgres-backups/"
        )



def dump_database():
    print("\U0001F4E6 Preparing database backup started")
    dump_db_operation_status = os.WEXITSTATUS(os.system(
        f'curl -X POST \
    -F "master_pwd={MASTER_PASSWORD}" \
    -F "name={ODOO_DATABASE_NAME}" \
    -F "backup_format=zip" \
    -o {ODOO_DATABASE_FILE_NAME}.$(date +%F).zip \
    http://storyka.ru/web/database/backup'
    ))
    if dump_db_operation_status != 0:
        exit(f"\U00002757 Dump database command exits with status "
             f"{dump_db_operation_status}.")
    print("\U0001F510 DB dumped, archieved and encoded")


def get_s3_instance():
    session = boto3.session.Session()
    return session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net'
    )


def upload_dump_to_s3():
    print("\U0001F4C2 Starting upload to Object Storage")
    get_s3_instance().upload_file(
        Filename=ODOO_DATABASE_FILE_NAME,
        Bucket=S3_BUCKET_NAME,
        Key=f'db-{get_now_datetime_str()}.zip'
    )
    print("\U0001f680 Uploaded")


def remove_temp_files():
    os.remove(ODOO_DATABASE_FILE_NAME)
    print(colored("\U0001F44D That's all!", "green"))


if __name__ == "__main__":
    say_hello()
    # check_key_file_exists()
    dump_database()
    upload_dump_to_s3()
    remove_temp_files()
