### 注册接口

#### request 请求

	POST /user/regist/

#### params参数

	mobile str 电话号码
	password str 密码
	password2 str 确认密码

#### response响应

失效响应1：

	{
	    "code": 1001,
	    "msg": "注册信息不能为空"
	}

失效响应2：

	{
	    "code": 1002,
	    "msg": "手机号码已经存在"
	}

失效响应3：

	{
	    "code": 1003,
	    "msg": "手机号码已存在"
	}

失效响应4：

	{
	    "code": 1004,
	    "msg": "两次密码不一致"
	}

成功响应：

	{
	    "code": 200,
	    "msg": "请求成功"
	}