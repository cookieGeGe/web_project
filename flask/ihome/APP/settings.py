import os

from APP.functions import get_db_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

templates_dir = os.path.join(BASE_DIR, 'templates')

static_dir = os.path.join(BASE_DIR, 'static')

upload_dir = os.path.join(static_dir, 'uploads')

DATABASE = {
    # 用户
    'USER': 'root',
    # 主机
    'HOST': '47.106.81.203',
    # 密码
    'PASSWORD': 'admin@123',
    # 端口
    'PORT': '3306',
    # 数据库类型
    'DB': 'mysql',
    # 数据库驱动
    'DRIVER': 'pymysql',
    # 使用的数据库
    'NAME': 'ihome',
}

# 连接数据库
SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)