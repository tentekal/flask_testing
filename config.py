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
	SQLALCHEMY_DATABASE_URI = os.environ.get("")

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = ""

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = ""


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'proudction': ProductionConfig,

	'default': DevelopmentConfig
}
