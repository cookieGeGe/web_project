#### 发布新房源接口信息

#### 发布新房源request请求：

	POST /house/newhouse/

#### 发布新房源response响应：

失效响应1：

	{
		'code': 2002, 
		'msg': '请将全部信息填写完整后再提交',
	}

失效响应2：

	{
	    "code": 900,
	    "msg": "数据库连接错误",
	}

成功响应：

	{
		'code': 200,
		'houseid': 9,
	}

#### 添加新房源图片request请求:

	PUT /house/newhouse/?id=

#### params参数

	id int 发布的新房源ID

#### 添加新房源图片response响应：

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误",
	}

失效响应2：

	{
		'code': 2003, 
		'msg': '请选择房屋图片后上传'
	}

失效响应3：

	{
		'code': 2004, 
		'msg': '上传图片类型错误'
	}

成功响应：

{
	'code': 200,
	'imgurl': '/static/upload/4.png',
}