### 房源信息详情

#### 获取房源信息详情request请求

	GET /house/details/?id=

#### params参数

	id int 房屋ID

#### 获取房源信息response响应：

失效响应1：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}


成功响应：

	{
	  "code": 200, 
	  "house": {
	    "acreage": 120, 
	    "address": "\u5929\u5e9c\u4e8c\u8857", 
	    "beds": "\u53cc\u4eba\u5e8a2x1.8", 
	    "capacity": 5, 
	    "deposit": 1000, 
	    "facitities": [
	      {
	        "css": "wirelessnetwork-ico", 
	        "id": 1, 
	        "name": "\u65e0\u7ebf\u7f51\u7edc"
	      }, 
	      {
	        "css": "shower-ico", 
	        "id": 2, 
	        "name": "\u70ed\u6c34\u6dcb\u6d74"
	      }, 
	      {
	        "css": "aircondition-ico", 
	        "id": 3, 
	        "name": "\u7a7a\u8c03"
	      }, 
	      {
	        "css": "icebox-ico", 
	        "id": 13, 
	        "name": "\u51b0\u7bb1"
	      }, 
	      {
	        "css": "washer-ico", 
	        "id": 14, 
	        "name": "\u6d17\u8863\u673a"
	      }, 
	      {
	        "css": "parkingspace-ico", 
	        "id": 20, 
	        "name": "\u505c\u8f66\u4f4d"
	      }, 
	      {
	        "css": "wirednetwork-ico", 
	        "id": 21, 
	        "name": "\u6709\u7ebf\u7f51\u7edc"
	      }, 
	      {
	        "css": "tv-ico", 
	        "id": 22, 
	        "name": "\u7535\u89c6"
	      }
	    ], 
	    "id": 11, 
	    "images": [
	      "/static/uploads/home01.jpg", 
	      "/static/uploads/home02.jpg", 
	      "/static/uploads/home03.jpg"
	    ], 
	    "max_days": 0, 
	    "min_days": 10, 
	    "order_count": 0, 
	    "price": 900, 
	    "room_count": 5, 
	    "title": "\u6b22\u4e50\u65f6\u5149", 
	    "unit": "\u56db\u5ba4\u4e24\u5385\u4e24\u536b", 
	    "user_avatar": "/static/uploads/landlord01.jpg", 
	    "user_name": "\u5927\u4fa0"
	  }, 
	  "is_self": 1
	}
