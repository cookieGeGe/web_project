### 我的房源页面接口

#### 实名验证request请求：

	GET /house/auth/

#### 实名验证response响应

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

失效响应2：

	{
		'code': 2001, 
		'msg': '用户没有完成实名制'
	}

有效响应：

	{
	  "code": 200, 
	  "msg": "请求成功"
	}


#### 房屋信息展示request请求：

	GET /house/auth_house/

#### 房屋信息展示response响应：

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

有效响应：

	{
	  "code": 200, 
	  "house_list": [
	    {
	      "address": "\u5929\u5e9c\u4e09\u8857", 
	      "area": "\u9ad8\u65b0\u533a", 
	      "create_time": "2018-05-22 20:39:38", 
	      "id": 7, 
	      "image": "/static/uploads/4.PNG", 
	      "order_count": 0, 
	      "price": 900, 
	      "room": 4, 
	      "title": "\u7231\u60c5"
	    }
	  ]
	}