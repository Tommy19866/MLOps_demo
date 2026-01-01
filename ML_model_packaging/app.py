import os
from config import ProductionConfig,DevelopmentConfig,TestingConfig

def run_app():
    env = os.getenv('ENV', 'development').strip().lower()

    print("DEBUG ENV =", repr(env))

    if env=='development':
        config=DevelopmentConfig()
    elif env=='production':
        config=ProductionConfig()
    elif env=='testing':
        config=TestingConfig()
    else :
        raise ValueError("Invalid environment name")
    
    print(f"running in {env} environment")
    print(f"debug: {config.DEBUG}")
    print(f"TESTING: {config.TESTING}")
    print(f"DATABASE_URI: {config.DATABASE_URI}")
    print(f"LOG_LEVEL: {config.LOG_LEVEL}")
    print(f"LOGFILE_PATH: {config.LOG_FILE_PATH}")
    print(f"SECRET_KEYS: {config.SECRET_KEY}")
    print(f"SECRET_COOKIES: {config.SECRET_COOKIES}")
    print(f"API_ENDPOINT: {config.API_ENDPOINT}")

if __name__=="__main__":
    run_app()
