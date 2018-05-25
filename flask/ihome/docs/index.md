### 主页接口信息

#### 主页展示信息request请求：

	GET /index/getarea/

#### 主页展示信息response响应：

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
	  "area": [
	    {
	      "id": 1, 
	      "name": "\u9526\u6c5f\u533a"
	    }, 
	    {
	      "id": 2, 
	      "name": "\u91d1\u725b\u533a"
	    }, 
	    {
	      "id": 3, 
	      "name": "\u9752\u7f8a\u533a"
	    }, 
	    {
	      "id": 4, 
	      "name": "\u9ad8\u65b0\u533a"
	    }, 
	    {
	      "id": 5, 
	      "name": "\u6b66\u4faf\u533a"
	    }, 
	    {
	      "id": 6, 
	      "name": "\u5929\u5e9c\u65b0\u533a"
	    }, 
	    {
	      "id": 7, 
	      "name": "\u53cc\u6d41\u53bf"
	    }, 
	    {
	      "id": 8, 
	      "name": "\u6210\u534e\u533a"
	    }, 
	    {
	      "id": 9, 
	      "name": "\u9752\u767d\u6c5f\u533a"
	    }, 
	    {
	      "id": 10, 
	      "name": "\u65b0\u90fd\u533a"
	    }, 
	    {
	      "id": 12, 
	      "name": "\u6e29\u6c5f\u533a"
	    }, 
	    {
	      "id": 13, 
	      "name": "\u90eb\u53bf"
	    }, 
	    {
	      "id": 14, 
	      "name": "\u84b2\u6c5f\u53bf"
	    }, 
	    {
	      "id": 15, 
	      "name": "\u5927\u9091\u53bf"
	    }, 
	    {
	      "id": 16, 
	      "name": "\u65b0\u6d25\u53bf"
	    }
	  ], 
	  "code": 200, 
	  "house": [
	    {
	      "address": "\u5929\u5e9c\u56db\u8857", 
	      "area": "\u5929\u5e9c\u65b0\u533a", 
	      "create_time": "2018-05-25 08:31:52", 
	      "id": 18, 
	      "image": "/static/uploads/6.jpg", 
	      "order_count": 0, 
	      "price": 300, 
	      "room": 3, 
	      "title": "\u5982\u5bb6"
	    }, 
	    {
	      "address": "\u9526\u57ce\u5e7f\u573a", 
	      "area": "\u5929\u5e9c\u65b0\u533a", 
	      "create_time": "2018-05-25 08:31:52", 
	      "id": 17, 
	      "image": "/static/uploads/9.jpg", 
	      "order_count": 0, 
	      "price": 168, 
	      "room": 3, 
	      "title": "\u5b9c\u5bb6"
	    }, 
	    {
	      "address": "\u5357\u718f\u5927\u9053", 
	      "area": "\u6e29\u6c5f\u533a", 
	      "create_time": "2018-05-25 08:31:52", 
	      "id": 16, 
	      "image": "/static/uploads/2.jpg", 
	      "order_count": 0, 
	      "price": 150, 
	      "room": 3, 
	      "title": "\u9633\u5149\u57ce"
	    }
	  ], 
	  "users": {
	    "avatar": "/static/uploads/logo@128x59.png", 
	    "id": 3, 
	    "name": "\u7231\u5bb6", 
	    "phone": "18512341234"
	  }
	}
