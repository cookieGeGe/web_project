from index.views import indexs
from myhouse.views import myhouse
from orders.views import orders
from user.views import users


def blue_regist(app):
    app.register_blueprint(users, url_prefix='/user')
    app.register_blueprint(myhouse, url_prefix='/house')
    app.register_blueprint(orders, url_prefix='/order')
    app.register_blueprint(indexs, url_prefix='/index')
