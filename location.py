#encoding=utf-8
#加入数学模块 和 数据库模块
import math
import sqlite3
from sql import sql_insert
#下面是 连接数据库 
connt = sqlite3.connect('mac_dtc.db')
c = connt.cursor()
#get_location
#参数distance1 是 sta与 ap1 的距离 
#参数distance2 是 sta与 ap2 的距离
#参数mac 是sta的物理地址
# 函数功能是 实现三边定位算法 得到 sta的二维坐标，并将数据插入数据库中
def get_location(distance1,distance2,distance3,mac):
	#下面是三个ap的具体坐标
	x1 = float(0)
	x2 = float(3)
	x3 = float(3)
	y1 = 4.0
	y2 = 4.0
	y3 = 0.0
#	distance1 = input("d1:")
#	distance2 = input("d2:")
#	distance3 = input("d3:")
	A = x1 - x3
	B = y1 - y3
	C = pow(x1,2)-pow(x3,2) + pow(y1,2) - pow(y3,2)+distance3-distance1
	D = x2-x3
	E = y2 - y3
	F = pow(x2,2)-pow(x3,2) + pow(y2,2) - pow(y3,2)+distance3-distance2
	x =  (B * F - E * C) / (2 * B * D - 2 * A * E)
	y =   (A * F - D * C) / (2 * A * E - 2 * B * D)
	print 'x,y:',x,y
	#将数据插入 数据库中
	sql_insert(connt,c,str(mac),str(x),str(y))
	pass
#get_location(6.25,15.25,11.25,"0:0:1:1")
