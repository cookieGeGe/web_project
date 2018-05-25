### 用户信息界面接口

#### GET请求

	GET /user/user_info/

#### response响应

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接失败"
	}

成功响应：

	{
	    "code": 200,
	    "user": {
			"id": XXX,
			"phone":xxx,
			"name": xxx,
			"avatar": xxx,
		}
	}