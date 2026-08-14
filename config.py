import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///app.db'
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

    @staticmethod
    def init_app(app):
        app.config.from_object(Config)
        app.secret_key = Config.SECRET_KEY
