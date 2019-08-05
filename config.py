import os

class Config:

   
    SECRET_KEY = ('kamikaze')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/pitch_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}