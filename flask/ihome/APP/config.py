import redis

from APP.settings import SQLALCHEMY_DATABASE_URI


class Config(object):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'
    SESSION_KEY = 'scret_key'
    SESSION_KEY_PREFIX = 'S_IH_AJ'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')
