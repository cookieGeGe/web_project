from flask import session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import functools

from werkzeug.utils import redirect


def get_db_uri(DATABASE):
    user = DATABASE.get('USER')
    passwd = DATABASE['PASSWORD']
    host = DATABASE['HOST']
    port = DATABASE['PORT']
    name = DATABASE['NAME']
    db = DATABASE['DB']
    driver = DATABASE['DRIVER']

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, passwd,
                                           host, port,
                                           name)


db = SQLAlchemy()


# session = Session()


def init_ext(app):
    db.init_app(app)
    # session.init_app(app)
    Session(app)


def is_login(view):
    @functools.wraps(view)
    def decorator(*args, **kwargs):
        try:
            # 验证用户是否登录
            # if session['user_id']:
            if 'user_id' in session:
                return view(*args, **kwargs)
            else:
                return redirect('/user/login/')

        except:
            return redirect('/user/login/')

    return decorator
