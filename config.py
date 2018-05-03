import os 
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    SECRET_KEY = os.environ.get('SECRET KEY') or '486217eU9f0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
    	pass


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get("postgresql://tentakel:Squ1ddles@127.0.0.1:5432/dvdrental")

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgresql://tentakel:Squ1ddles@127.0.0.1:5432/dvdrental"

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = "postgresql://tentakel:Squ1ddles@127.0.0.1:5432/dvdrental"


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'proudction': ProductionConfig,

	'default': DevelopmentConfig
}