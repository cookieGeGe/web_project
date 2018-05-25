### 预定房间接口信息

#### 返回预定房间信息request请求

	GET /house/books/<int:id>/

#### params参数

	id int 房屋ID

#### 预定房屋response响应：

失效响应：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

有效响应




#### 提交订单request请求：

	POST /order/

#### params参数

	id int 房屋ID
	start_date str 入住时间
	end_date str 离开时间

#### 提交订单response响应：

失效响应1：

	{
		'code': 3001, 
		'msg': '入住起止时间不能为空'
	}

失效响应2：

	{
		'code': 3002, 
		'msg': '起止时间错误'
	}

失效响应3：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

有效响应：

	{
		'code': 200, 
		'msg': '请求成功'
	}