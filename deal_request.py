#encoding=utf-8
import re
import location
import sqlite3
from collections import Counter
from location import get_location
from sql import sql_look
res = ' '
import json as js

_name_ = '_main_'
#iii = 'POST /XY HTTP/1.1\r\n{[{\'mac\':\'0:0:11:0\',\'d1\':4.0,\'d2\':5.0,\'d3\':3.0}]}'
#ii = 'GET /XY HTTP/1.1\r\nMAC:0:0:0:1\r\n'
def get_re_data(re_data):
	tmp = js.dumps(re_data)
	temp_dt = str(js.loads(tmp))
	pattern = re.compile(r'({.*?})')
	x = pattern.findall(temp_dt)  
	num = Counter(x)
	for i in num:	
		print i
		tmps = js.dumps(i)
		print tmps
		pattern = re.compile(r'\:\'(.*?)\'\,')
		mac_data = pattern.findall(tmps)
		pattern = re.compile(r'\:(.*?)\,')
		deal_data = pattern.findall(tmps)
		pattern = re.compile(r'.*\,.*\,.*\,.*\:(.*?)}')
		last_data = pattern.findall(tmps)
		print  deal_data[1]
		print  deal_data[2]
		print  last_data[0]
		print  mac_data[0]
		get_location(float(deal_data[1]),float(deal_data[2]),float(last_data[0]),mac_data[0])		
		
	pass
def get_re_data1(re_data):
	pattern = re.compile(r'MAC:(.*?)\r\n')
	x = pattern.findall(re_data)  
	num = Counter(x)
	connt = sqlite3.connect('mac_dtc.db')
	c = connt.cursor()
	for i in num:	
		print i
		res = sql_look(connt,c,i)
	print res
	print res[0]
	print type(res)
	print type(res[0])
	print  res[0][0]
	print  res[0][1]
	print  res[0][2]
	reback_data = '[MAC:'+str(res[0][0]) +',TIME:'+str(res[0][1])+',X:'+str(res[0][2])+',Y:'+str(res[0][3])+']'
	print reback_data
	return reback_data

def deals_request(rcv_data):
	cmd = re.match(r"([^ ]*) ",rcv_data).group(1)
	types = re.match(r"\w+ +/+([^ ]*) ",rcv_data).group(1)
	print cmd,types
	p = re.compile(r'{(.*\])')
	body = p.findall(rcv_data)
	if cmd == 'POST' and types == 'XY':
		get_re_data(body[0])
	if cmd == 'GET' and types == 'XY':
		return	get_re_data1(rcv_data)
	pass
#if _name_ == '_main_':
#	deals_request(ii)

