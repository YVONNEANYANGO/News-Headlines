import os

class Config:

    base_url='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
        # TOP_HEADLINES_BASE_URL = 

    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    pass



class DevConfig(Config):

    pass

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}