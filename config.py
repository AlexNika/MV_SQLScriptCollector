import os


class Config:
    DEBUG = True
    SECRET_KEY = 'a really really really really long secret key'
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = f'sqlite+pysqlite:///{os.path.abspath(os.getcwd())}\\mvm_sql_scripts.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
