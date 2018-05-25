### 我的订单页面接口信息

#### 获取我的订单request请求：

	GET /order/myorders/

#### 获取我的订单response请求：

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
	  "code": 200, 
	  "order": [
	    {
	      "amount": 900, 
	      "begin_date": "2018-05-23", 
	      "comment": null, 
	      "create_date": "2018-05-23", 
	      "days": 1, 
	      "end_date": "2018-05-23", 
	      "house_title": "\u6b22\u4e50\u65f6\u5149", 
	      "image": "/static/uploads/home01.jpg", 
	      "order_id": 5, 
	      "status": "WAIT_ACCEPT"
	    }, 
	    {
	      "amount": 6300, 
	      "begin_date": "2018-05-24", 
	      "comment": null, 
	      "create_date": "2018-05-23", 
	      "days": 7, 
	      "end_date": "2018-05-30", 
	      "house_title": "\u6b22\u4e50\u65f6\u5149", 
	      "image": "/static/uploads/home01.jpg", 
	      "order_id": 6, 
	      "status": "WAIT_ACCEPT"
	    }
	  ]
	}
