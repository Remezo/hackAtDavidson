
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
