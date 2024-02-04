
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_API_KEY= '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
