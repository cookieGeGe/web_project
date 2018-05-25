import re

import os
from flask import Blueprint, render_template, request, jsonify, session, redirect

from APP.models import db, User
from APP.settings import upload_dir
from utils.status_code import SUCCESS, USER_REGISTER_PARAMS_ERROR, \
    USER_REGISTER_MOBILE_ERROR, USER_REGISTER_MOBILE_IS_EXISTS, \
    USER_REGISTER_CHECK_PASSWORD, DATABASE_ERROR, USER_LOGIN_MOBILE_IS_NOT_EXISTS, \
    USER_LOGIN_PASSWORD_ERROR
from utils import status_code
from APP.functions import is_login

users = Blueprint('user', __name__)


@users.route('/createdb/')
# @is_login
def create_db():
    db.create_all()
    return '创建成功'


# 注册页面
@users.route('/regist/', methods=['GET'])
def regist():
    return render_template('register.html')


# 注册请求
@users.route('/regist/', methods=['POST'])
def user_regist():
    user_dict = request.form
    mobile = user_dict['mobile']
    pwd = user_dict['password']
    pwd2 = user_dict['password2']

    # 验证传入参数是否为空
    if not all([mobile, pwd, pwd2]):
        return jsonify(USER_REGISTER_PARAMS_ERROR)
    # 验证手机号是否符合规则
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(USER_REGISTER_MOBILE_ERROR)
    # 验证用户是否已经存在
    if not User.query.filter(User.phone).count():
        return jsonify(USER_REGISTER_MOBILE_IS_EXISTS)
    # 验证两次用户名和密码是否相同
    if pwd != pwd2:
        return jsonify(USER_REGISTER_CHECK_PASSWORD)

    user = User()
    user.phone = mobile
    user.name = mobile
    user.password = pwd

    try:
        user.add_update()
        return jsonify(SUCCESS)
    except:
        return jsonify(DATABASE_ERROR)


# 登录页面
@users.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


# 登录页面
@users.route('/login/', methods=['POST'])
def user_login():
    user_dict = request.form
    mobile = user_dict.get('mobile')
    password = user_dict.get('password')

    if not all([mobile, password]):
        return jsonify(USER_REGISTER_PARAMS_ERROR)
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(status_code.USER_LOGIN_MOBILE_ERROR)
    if not User.query.filter(User.phone).count():
        return jsonify(USER_LOGIN_MOBILE_IS_NOT_EXISTS)
    user = User.query.filter(User.phone == mobile).first()
    if user.check_pwd(password):
        session['user_id'] = user.id
        return jsonify(SUCCESS)
    else:
        return jsonify(USER_LOGIN_PASSWORD_ERROR)


@users.route('/my/')
@is_login
def my_info():
    return render_template('my.html')


@users.route('/user_info/')
@is_login
def user_info():
    user_id = session['user_id']
    try:
        user = User.query.get(user_id)
        return jsonify(user=user.to_basic_dict(), code=200)
    except:
        return jsonify(DATABASE_ERROR)


@users.route('/profile/', methods=['GET'])
@is_login
def profile():
    return render_template('profile.html')


@users.route('/profile/', methods=['PUT'])
@is_login
def user_profile():
    file = request.files

    # 判断上传的文件是否为空
    if 'avatar' in file:
        image_file = file['avatar']
        if not re.match('^image/.*$', image_file.mimetype):
            return jsonify(status_code.USER_UPLOAD_IMG_TYPE_ERROR)
        img_name = image_file.filename
        url = os.path.join(upload_dir, img_name)
        # 保存图片
        image_file.save(url)

        user_id = session['user_id']
        user = User.query.get(user_id)
        img_url = os.path.join('/static/uploads/', img_name)
        try:
            user.avatar = img_url
            user.add_update()
            return jsonify(code=status_code.OK, img_url=img_url)
        except:
            return jsonify(DATABASE_ERROR)
    else:
        return jsonify(status_code.USER_UPLOAD_IMG_ERROR)


@users.route('/profile/name/', methods=['POST'])
@is_login
def user_text_profile():
    username = request.form.get('name')
    if not all([username, ]):
        return jsonify(status_code.USER_UPLOAD_NAME_ERROR)
    if User.query.filter(User.name == username).count():
        return jsonify(status_code.USER_UPLOAD_NAME_IS_EXISTS)
    user_id = session['user_id']
    user = User.query.get(user_id)
    try:
        user.name = username
        user.add_update()
        return jsonify(SUCCESS)
    except:
        return jsonify(DATABASE_ERROR)


@users.route('/userauth/', methods=['GET'])
@is_login
def user_auth():
    return render_template('auth.html')


@users.route('/userauth/', methods=['POST'])
@is_login
def user_auths():
    real_name = request.form.get('real-name')
    real_number = request.form.get('id-card')
    if not all([real_name, real_number]):
        return jsonify(status_code.USER_REALINFO_ERROR)
    if len(real_number) != 18:
        return jsonify(status_code.USER_REAL_ID_ERROR)
    user_id = session.get('user_id')
    try:
        user = User.query.get(user_id)
        user.id_name = real_name
        user.id_card = real_number
        user.add_update()
        return jsonify(status=SUCCESS, card=real_number, real_name=real_name)
    except:
        return jsonify(DATABASE_ERROR)


@users.route('/realinfo/')
@is_login
def realinfo():
    user_id = session['user_id']
    user = User.query.get(user_id)
    if user.id_name == None or user.id_card == None:
        return jsonify(status_code.USER_REAL_IS_NULL)
    else:
        card = user.id_card
        real_name = user.id_name
        return jsonify(status=SUCCESS, card=card, real_name=real_name)

@users.route('/logout/')
@is_login
def logout():
    session.clear()
    return jsonify(SUCCESS)