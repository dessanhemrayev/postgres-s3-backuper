Backup and restore PostgreSQL database with Yandex Object Storage (or any S3-compatible storage)
===

There are two Python scripts: `main.py`. This script one creates
PostgreSQL dump, zip and then upload to Yandex Object
Storage (or any S3-compatible storage). 

[YouTube video about scripts (in Russian)](https://www.youtube.com/watch?v=30TBpI4lEPI)

For both scripts you need:

* Python3.6+ version,
* installed pip packeges from `requirements.txt`,
* Yandex Object Storage / AWS credentials in `~/.aws/credentials`,


Example of backup database (substitute your values in the variables below,
note, that here we need public key file for encrypting database):

```sh
DB_HOSTNAME=localhost \
DB_NAME=your_database  \
DB_USER=your_db_user  \
S3_BUCKET_NAME=your_s3_bucket  \
TIME_ZONE=Europe/Moscow \
python3 main.py
```
Status of last Deployment:<br>
<img src="https://github.com/dessanhemrayev/postgres-s3-backuper/workflows/Backup_yandex_object_Storage/badge.svg?branch=main"><br>

Borrowed from the author [https://github.com/alexey-goloburdin](https://github.com/alexey-goloburdin)
