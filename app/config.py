import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql://root:root@localhost/prueba'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
