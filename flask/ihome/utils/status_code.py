OK = 200
SUCCESS = {'code': 200, 'msg': '请求成功'}
DATABASE_ERROR = {'code': 900, 'msg': '数据库连接失败'}

# 用户模块

USER_REGISTER_PARAMS_ERROR = {'code': 1000, 'msg': '注册信息不能为空'}
USER_REGISTER_MOBILE_ERROR = {'code': 1001, 'msg': '手机号码不能为空'}
USER_REGISTER_MOBILE_IS_EXISTS = {'code': 1002, 'msg': '手机号码已经存在'}
USER_REGISTER_CHECK_PASSWORD = {'code': 1003, 'msg': '两次密码不一致'}

USER_LOGIN_MOBILE_IS_NOT_EXISTS = {'code': 1004, 'msg': '手机号码不存在'}
USER_LOGIN_MOBILE_ERROR = {'code': 1013, 'msg': '手机号码错误'}
USER_LOGIN_PASSWORD_ERROR = {'code': 1005, 'msg': '密码错误'}

USER_UPLOAD_IMG_ERROR = {'code': 1006, 'msg': '上传的图像不能为空'}
USER_UPLOAD_IMG_TYPE_ERROR = {'code': 1007, 'msg': '上传的图像类型错误'}

USER_UPLOAD_NAME_ERROR = {'code': 1008, 'msg': '用户名不能为空'}
USER_UPLOAD_NAME_IS_EXISTS = {'code': 1009, 'msg': '用户名已经存在'}

USER_REALINFO_ERROR = {'code': 1010, 'msg': '实名信息不能为空'}
USER_REAL_ID_ERROR = {'code': 1011, 'msg': '身份证ID号错误'}

USER_REAL_IS_NULL = {'code': 1012, 'msg': '实名认证未完成'}

HOUSE_USER_AUTH_IS_NULL = {'code': 2001, 'msg': '用户没有完成实名制'}

HOUSE_UPLOAD_INFO_ERROR = {'code': 2002, 'msg': '请将全部信息填写完整后再提交'}

HOUSE_UPLOAD_IMG_ERROR = {'code': 2003, 'msg': '请选择房屋图片后上传'}
HOUSE_UPLOAD_IMG_TYPE_ERROR = {'code': 2004, 'msg': '上传图片类型错误'}

ORDER_COMMIT_IS_NULL = {'code': 3001, 'msg': '入住起止时间不能为空'}
ORDER_COMMIT_TIME_ERROR = {'code': 3002, 'msg': '起止时间错误'}
