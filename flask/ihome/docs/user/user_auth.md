### 用户实名认证

#### 用户实名认证request请求:

	GET /user/realinfo/

#### 用户实名认证response响应：

失效响应1：

	{
		'code': 1012, 
		'msg': '实名认证未完成'
	}

成功响应：

	{
		'card':xxxx 用户真实ID,
		'real_name': xxxx 用户真实姓名,
		'status':{
			"code": 200,
			"msg": "请求成功"
		}
	}


#### 实名认证request请求:

	POST /user/userauth/

#### params参数
	
	real-name str 用户真实姓名
	id-card str 用户身份证号码

#### 实名认证response响应：

失效响应1：

	{
		'code': 1010, 
		'msg': '实名信息不能为空'
	}

失效响应2：

	{
		'code': 1011, 
		'msg': '身份证ID号错误'
	}

失效响应3：

	{
	    "code": 900,
	    "msg": "数据库连接错误"
	}

成功响应：

	{
		'card':xxxx 用户真实ID,
		'real_name': xxxx 用户真实姓名,
		'status':{
			"code": 200,
			"msg": "请求成功"
		}
	}