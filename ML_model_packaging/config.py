class Config:
    DEBUG=False
    TESTING=False
    DATABASE_URI="sqlite:///:memory:"
    LOG_LEVEL='DEBUG'
    LOG_FILE_PATH='app.log'
    SECRET_KEY='mysecretkey'
    SECRET_COOKIES='mysecretcookies'
    API_ENDPOINT='https://api.example.com'

class ProductionConfig(Config):
    DATABASE_URI="sqlite:///:memory:"
    LOG_LEVEL='DEBUG'
    LOG_FILE_PATH='app.log'
    SECRET_KEY='mysecretkey'
    SECRET_COOKIES='mysecretcookies'
    API_ENDPOINT='https://api.example.com'

class DevelopmentConfig(Config):
    DEBUG=True
    LOG_LEVEL='INFO'
    LOG_FILE_PATH='app.log'
    SECRET_KEY='mysecretkey_dev'
    SECRET_COOKIES='mysecretcookies'
    API_ENDPOINT='https://api.example.com'

class TestingConfig(Config):
    TESTING=False
    LOG_LEVEL='INFO'
    LOG_FILE_PATH='app.log'
    SECRET_KEY='mysecretkey_dev'
    SECRET_COOKIES='mysecretcookies'
    API_ENDPOINT='https://api.example.com'





#production testing development env
#different stages of your project
