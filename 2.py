# -*- coding: UTF-8 -*- 
from __future__ import division 
import web
import json
import sys  
import codecs  
import operator
import MySQLdb
from datetime import datetime
 
import traceback
reload(sys)  
sys.setdefaultencoding('utf-8')  
urls = (
    '/', 'index',
     '/consult', 'consult',
	 '/complain', 'complain',
	 '/praise', 'praise',
	 '/service', 'service',
	 '/customers', 'customers',
	 '/goods', 'goods',
	 '/congoods', 'congoods',
	 '/conservice', 'conservice',
	 '/conlog', 'conlog',
	 '/conactivity', 'conactivity',
)

#页面初始化时的图表
class index:
    def GET(self):
        web.header('content-type','text/json')
        web.header("Access-Control-Allow-Origin", "*")
        dic={"data1":['线上活动','积分活动','系统操作','PM推送活动规则','活动参与方式','奖品配送规则','小积分抽奖规则','会员绑定方式'],\
		"data2":[{'name':"线上活动",'value': 70},{'name':"积分活动",'value': 60},{'name':"系统操作",'value': 80}],\
		"data3":[{'name':"PM推送活动规则",'value': 70},{'name':"活动参与方式",'value': 60},{'name':"奖品配送规则",'value': 80},\
		{'name':"小积分抽奖规则",'value':60},{'name':"会员绑定方式",'value':50}],}
        return json.dumps(dic)
		
    def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print data
		data={"data1":{"佳洁士": 70,"高露洁": 60,"蓝月亮": 80,"雕牌":50,"力士":60,"多芬":65},\
		"data2":{"优惠活动": 70,"代言人": 60,"产品质量": 80,},}
		return json.dumps(data) 

    def OPTIONS(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
        web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

#Consult咨询生成的图表
class consult:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		FirstDiv='咨询'
		FirstDiv=str(FirstDiv)
		print data

		#获取起始日期和结束日期
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		#连接数据库
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#查询并计算一级分类为“咨询”下的二级分类并统计个数
		sql="select SecondDiv,count(SecondDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by SecondDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list.append(result)
		d1=[x['name'] for x in div_list]


		#查询并计算一级分类为“咨询”下的三级分类并统计个数
		sql="select ThirdDiv,count(ThirdDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by ThirdDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list1=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list1.append(result)
		
		d2=([x['name'] for x in div_list1])
		data1=d1+d2
		data={"data1":data1,"data2":div_list,"data3":div_list1}
		print(data1)
		return json.dumps(data)
		
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
		 
#Complain投诉生成的图表
class complain:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		FirstDiv='投诉'
		FirstDiv=str(FirstDiv)
		print data

		#获取起始日期和结束日期
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		#连接数据库
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#查询并计算一级分类为“投诉”下的二级分类，三级分类并统计个数
		sql="select SecondDiv,count(SecondDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by SecondDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list.append(result)
		d1=[x['name'] for x in div_list]


		#查询并计算一级分类为“投诉”下的三级分类并统计个数
		sql="select ThirdDiv,count(ThirdDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by ThirdDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list1=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list1.append(result)
		
		d2=([x['name'] for x in div_list1])
		data1=d1+d2
		data={"data1":data1,"data2":div_list,"data3":div_list1}
		print(data1)
		return json.dumps(data)
		
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

#Praise咨询生成的图表
class praise:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		FirstDiv='表扬'
		FirstDiv=str(FirstDiv)
		print data

		#获取起始日期和结束日期
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		#连接数据库
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#查询并计算一级分类为“表扬”下的二级分类，三级分类并统计个数
		sql="select SecondDiv,count(SecondDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by SecondDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list.append(result)
		d1=[x['name'] for x in div_list]


		#查询并计算一级分类为“表扬”下的三级分类并统计个数
		sql="select ThirdDiv,count(ThirdDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by ThirdDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list1=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list1.append(result)
		
		d2=([x['name'] for x in div_list1])
		data1=d1+d2
		data={"data1":data1,"data2":div_list,"data3":div_list1}
		print(data1)
		return json.dumps(data)
		
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
		 
#Service投诉生成的图表
class service:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		FirstDiv='服务'
		FirstDiv=str(FirstDiv)
		print data

		#获取起始日期和结束日期
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		#连接数据库
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#查询并计算一级分类为“服务”下的二级分类，三级分类并统计个数
		sql="select SecondDiv,count(SecondDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by SecondDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list.append(result)
		d1=[x['name'] for x in div_list]


		#查询并计算一级分类为“服务”下的三级分类并统计个数
		sql="select ThirdDiv,count(ThirdDiv) from rawtable where StartTime>'%s' \
		and EndTime<'%s' and FirstDiv='%s' group by ThirdDiv" % (startTime,endTime,FirstDiv)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list1=[]

		for row in rows:
			result={'name': str(row[0]), 'value': str(row[1])}
			div_list1.append(result)
		
		d2=([x['name'] for x in div_list1])
		data1=d1+d2
		data={"data1":data1,"data2":div_list,"data3":div_list1}
		print(data1)
		return json.dumps(data)
	
#重点客户和活跃客户生成的图表
class customers:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print data
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))

		div_list=[]
		
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#活跃客户(单位时间内会话次数和条数)
		sql="select CusName,count(distinct(ChatId)),count(distinct(SingleText)),\
		count(distinct(ChatId)) +count(distinct(SingleText)) from reconstable where StartTime>'%s' and EndTime<'%s'\
		group by CusName order by count(distinct(ChatId))+count(distinct(SingleText)) DESC" % (startTime,endTime)

		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		for row in rows:
			result={'cus2': str(row[0]), 'con2': int(row[3])}
			div_list.append(result)
		cus2=[x['cus2'] for x in div_list]
		con2=[x['con2'] for x in div_list]
		print div_list
		
		#重点客户(单位时间内会话次数和购买量)
		sql="select CusName,count(distinct(ChatId)) from reconstable \
		where StartTime>'%s' \
		and EndTime<'%s'  group by CusName order by count(distinct(ChatId)) DESC" % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		div_list1=[]
		for row in rows:
			result={'cus1': str(row[0]), 'con1': int(row[1])+10} #假设每个客户的购买量加权后，数值为10
			div_list1.append(result)
			
		
		cus1=[x['cus1'] for x in div_list1]
		con1=[x['con1'] for x in div_list1]

		data={"cus1":cus1,"con1":con1,"cus2":cus2,"con2":con2,}
		print(data)
		return json.dumps(data)
	
	def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		
		data={"cus1":['商品','活动','c','d','k','x'],"con1":[1,2,4,3,5,6],\
		"cus2":['商品','活动','c','d','k','x'],"con2":[6,2,4,3,5,6],}
		
		return json.dumps(data)
		
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

#热销商品生成的图表
class goods:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print(data)
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor() 
		
		#热销商品
		sql="select GoodsName,count(ChatId) from goodstable \
		where StartTime>'%s' and EndTime<'%s' \
		group by GoodsName order by count(ChatId) DESC" % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()

		div_list={}
		for row in rows:
			div_list[str(row[0])]= int(row[1])
			
		#div_list=sorted(div_list.iteritems(), key = operator.itemgetter(1), reverse = True)
		print div_list

		#单个商品热销分析
		Name='佳洁士'
		Name=str(Name)
		sql="select SaleReason,count(SaleReason) from goodstable \
		where StartTime>'%s' and EndTime<'%s' and GoodsName='%s' \
		group by SaleReason order by count(SaleReason) DESC" % (startTime,endTime,Name)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		div_list1={}
		for row in rows:
			div_list1[str(row[0])]= int(row[1])
		
		data={"data1":div_list,"data2":div_list1,}

		print(data)
		return json.dumps(data)
		
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

#商品满意度
class congoods:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print(data)
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor()
		
		#获取有关商品的总会话数
		sql="select count(ChatId) from goodstable where StartTime>'%s' \
		and EndTime<'%s' " % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		for row in rows:
			sum=int(row[0])
		
		#获取商品的负面评价的总会话数
		sql="select count(ChatId) from goodstable where StartTime>'%s' \
		and EndTime<'%s' and Emotion<0 " % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		div_list=[]
		x=0
		for row in rows:
			x=x+int(row[0])
		sum=round((sum-x)/sum,2)  #计算商品满意度

		#获取商品的描述关键词
		sql="select Description from goodstable where StartTime>'%s' \
		and EndTime<'%s' and Description is not null" % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		description=''
		for row in rows:
			description+=str(row[0])
			
		

		data={"data1":sum,"data2":description,}
		print data
		return json.dumps(data)
		
	def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data={"data1":0.7,"data2":'正品 正品 正品 正品 正品 实用 可靠 可靠 快捷 快捷 快捷'+\
		'精美 精美 精美 精美 方便 方便 方便 方便 品种齐全 品种齐全 大方 大方 耐用 耐用 耐用 耐用',}
		return json.dumps(data) 
	
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
	
#客服满意度
class conservice:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print(data)
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		#startTime='2017/11/1'
		#endTime='2017/11/28'
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor()
		
		#获取有关客服名及各自的总会话数
		sql="select SerName,count(ChatId) from servicetable where StartTime>'%s' \
		and EndTime<'%s' group by SerName " % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		div_list=[]
		div_list1=[]
		s='质量评分'
		item=0
		for row in rows:
			item=item+1
			name=str(row[0])
			sum= int(row[1])
			#计算投诉比
			sql2="select count(*) from servicetable where SerName='%s' and\
			StartTime>'%s' and EndTime<'%s'and Class='投诉'"% (str(row[0]),startTime,endTime)
			count2=cursor.execute(sql2)
			rows2=cursor.fetchall()
			for r in rows2:
				i=int(r[0])
			i=round(i/sum,2)
			
			#计算解答比
			sql3="select count(*) from servicetable where SerName='%s' and\
			StartTime>'%s' and EndTime<'%s'and Class='解答'"% (str(row[0]),startTime,endTime)
			count3=cursor.execute(sql3)
			rows3=cursor.fetchall()
			for r in rows3:
				j=int(r[0])
			j=round(j/sum,2)
			
			#计算用户反馈评分和回应时长的平均值
			sql4="select avg(CusScore),avg(ResTime) from servicetable where SerName='%s' and\
			StartTime>'%s' and EndTime<'%s'"% (str(row[0]),startTime,endTime)
			count4=cursor.execute(sql4)
			rows4=cursor.fetchall()
			for r in rows4:
				score=int(r[0])
				time=int(r[0])
				
			#总分=-10*投诉比+10*解答比+10*用户评分-5*回应时长
			totalscore=-10*i+10*j+10*score-5*time
			
			result=[name,i,j,score,time,totalscore]
	
			div_list.append(result)
			
			result2=[name,s,totalscore]
			div_list1.append(result2)
		
		div_list1.sort(key=lambda x:(x[2]),reverse=True)
		print div_list1,div_list
		data={"data1":div_list1,"data2":div_list}

		return json.dumps(data)
	
	def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		
		data1=[[1,"阿肯色","质量评分",90],[2,"李晓雪","质量评分",88],\
		[3,"王露露","质量评分",87],[4,"肖文青","质量评分",85],[5,"陈映宏","质量评分",83]]
		
		data2=[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
		data={"data1":data1,"data2":data2}
		
		return json.dumps(data) 
		#return data2
	
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
		
#物流满意度
class conlog:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print(data)
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor()
		
		sql="select count(ChatId) from logistictable where StartTime>'%s' \
		and EndTime<'%s' " % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		for row in rows:
			sum=int(row[0])
		
		sql="select Class,count(ChatId) from logistictable where StartTime>'%s' \
		and EndTime<'%s' and Emotion<0 group by Class" % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		div_list=[]
		x=0
		for row in rows:
			x=x+int(row[1])
			result={'name': str(row[0]), 'value': int(row[1])} 
			div_list.append(result)

		
		sum=round((sum-x)/sum,2)
		print sum
		data={"data1":sum,"data2":div_list,}
		print data
		return json.dumps(data)
		
	def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data={"data1":0.16,"data2":[{'value': 2154,'name': '发货速度慢'}, {'value': 3454,\
		'name': '运输时间长'}, {'value': 3015,'name': '消息更新延迟'}, \
		{'value': 3515,'name': '产品损坏'}, {'value': 3515,'name': '信息错误'}],}
		return json.dumps(data) 
	
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')

#活动满意度
class conactivity:
	def GET(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data=web.input()
		print(data)
		
		startTime=str(datetime.strptime(data["startTime"],"%Y/%m/%d"))
		endTime=str(datetime.strptime(data["endTime"],"%Y/%m/%d"))
		
		conn=MySQLdb.connect(  host='localhost',  port=3306,  user='root',  passwd='password',  db='new',charset='utf8') 
		cursor=conn.cursor()
		
		sql="select count(ChatId) from activitytable where StartTime>'%s' \
		and EndTime<'%s' " % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		for row in rows:
			sum=int(row[0])
		
		sql="select Class,count(ChatId) from activitytable where StartTime>'%s' \
		and EndTime<'%s' and Emotion<0 group by Class" % (startTime,endTime)
		count=cursor.execute(sql)
		rows=cursor.fetchall()
		
		div_list=[]
		d=[]
		x=0
		max=3
		for row in rows:
			x=x+int(row[1])
			result={'name': str(row[0]), 'max': max} 	
			div_list.append(result)
		
		print div_list
		for row in rows:
			r={'value': int(row[1])}
			d.append(r)
		d=[y['value'] for y in d]

		print d
		sum=round((sum-x)/sum,2)
		print sum
		data={"data1":sum,"data2":div_list,"data3":d,}
		print data
		return json.dumps(data)
		
	def POST(self):
		web.header('content-type','text/json')
		web.header("Access-Control-Allow-Origin", "*")
		data={"data1":0.17,"data2":[{'max': 100,'text': '审核进度较慢'}, {'max': 100,\
		'text': '积分兑换失败'}, {'max': 100,'text': '活动规则不明'}],"data3":[60,85,40],}
		return json.dumps(data) 
	
	def OPTIONS(self):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Headers',  'Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')
		web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
		
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
