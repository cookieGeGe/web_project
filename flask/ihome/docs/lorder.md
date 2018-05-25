### 客户订单页面接口信息

#### 获取客户订单request请求：

	GET /order/cus_orders/

#### 获取客户订单response响应：

失效响应：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

{
  "code": 200, 
  "lorders": [
    {
      "amount": 1000, 
      "begin_date": "2018-05-27", 
      "comment": null, 
      "create_date": "2018-05-25", 
      "days": 5, 
      "end_date": "2018-05-31", 
      "house_title": "7\u5929", 
      "image": "/static/uploads/home03.jpg", 
      "order_id": 7, 
      "status": "WAIT_ACCEPT"
    }
  ]
}

#### 客户订单页面接单和拒单request请求：

	PATCH /order/lorder/<id>/

#### params请求参数：

	id int 用户订单ID

#### 客户订单页面接单和拒单response请求：

失效响应：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
	    "code": 200,
	    "msg": "请求成功"
	}