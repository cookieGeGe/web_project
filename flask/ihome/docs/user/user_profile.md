### 修改用户个人信息接口：

#### 上传头像request请求：

	PUT /user/profile/

#### 上传头像response响应：

失效响应1：

	{
	    "code": 1006,
	    "msg": "上传头像不能为空"
	}

失效响应2：

	{
	    "code": 1007,
	    "msg": "上传的图像类型错误"
	}

失效响应3

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
	    "code": 200,
	    "img_url: 图片的保存路径,
	}

#### 修改名字request请求：

	POST /user/profile/name/

#### params参数

	name str 用户名

#### 修改名字response响应：

失效响应1：

	{
		'code': 1008, 
		'msg': '用户名不能为空,
	}

失效响应2：

	{
		'code': 1009, 
		'msg': '用户名已经存在'
	}

失效响应3：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
	    "code": 200,
	    "msg": "请求成功"
	}