
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
