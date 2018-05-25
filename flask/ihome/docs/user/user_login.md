### 登录接口

#### request 请求

	POST /user/login/

#### params参数

	mobile str 电话号码
	password str 密码

#### response响应

失效响应1：

	{
	    "code": 1001,
	    "msg": "注册信息不能为空"
	}

失效响应2：

	{
	    "code": 1013,
	    "msg": "手机号码错误"
	}

失效响应3：

	{
	    "code": 1004,
	    "msg": "手机号码不存在"
	}

失效响应4：

	{
	    "code": 1005,
	    "msg": "密码错误"
	}

成功响应：
	
	{
	    "code": 200,
	    "msg": "请求成功"
	}