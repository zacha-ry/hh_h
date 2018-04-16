#encoding=utf-8
import sqlite3
import time
ISOTIMEFORMAT='%Y-%m-%d %X'
connt = sqlite3.connect('mac_dtc.db')
c = connt.cursor()
#sql_insert 函数
#插入sta 数据 如果sta已经存在 那么更新数据 如果不存在 插入数据
#
def sql_insert(connt,c,mac,x,y):
	Time = '1'
	get_time = 'SELECT Time from text WHERE MAC =' +'\'' +mac +'\'' +';'
	cmd_sel = 'SELECT * from text WHERE MAC=' +'\'' +mac+'\''+ ';'
	print cmd_sel
	print '\n'
	time.time()
	Now = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
	cmd_ins = 'INSERT INTO text (MAC,Time,D1,D2)VALUES(' +'\''+ mac+'\'' +',' + Time + ',' +x + ',' +  y  +');' 
	cmd_upd = 'UPDATE text set Time =' + Time +',D1=' + x +',D2=' +y +',CreatedTime=\''+Now+'\'' +' WHERE MAC =' + '\'' +mac+'\'' + ';'
	print cmd_upd
	c.execute(cmd_sel);
	print(c.fetchmany(3)) 
	tt = (c.fetchmany(3) == '[]')
	print tt
	if tt:
		print cmd_ins
		c.execute(cmd_ins)
		print(c.fetchmany(3)) 
	else:
		print cmd_upd
		c.execute(cmd_upd)	
		print(c.fetchmany(3)) 
	connt.commit()
	pass
#查询数据 如果没有返回none 如果有返回数据 查询最近的数据
def sql_look(connt,c,mac):
	end_s = time.time() + 20
	begin_s = end_s - 400000
	end = time.strftime( ISOTIMEFORMAT, time.localtime(end_s))
	begin = time.strftime( ISOTIMEFORMAT, time.localtime(begin_s))
	cmd_sel = 'select MAC,Time,D1,D2 from text where MAC = '+'\''+ mac+'\'' +' and CreatedTime Between '+ 'datetime(\''+begin+'\') and datetime(\'' + end +'\');'

#	cmd_sel = 'select MAC,Time,D1,D2 from text where CreatedTime Between '+ 'datetime(\''+begin+'\') and datetime(\'' + end +'\');'
	print cmd_sel
	c.execute(cmd_sel)
	result = (c.fetchmany(3))
	print result	
	return result
	pass
#sql_insert(connt,c,'0:0:2:1',str(2.0),str(1.0));
#sql_look(connt,c,'0:0:2:1');
	
