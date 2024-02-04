
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
