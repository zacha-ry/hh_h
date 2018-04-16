#econding=utf-8
import time 
ISOTIMEFORMAT='%Y-%m-%d %X'
begin=time.time()
end = begin - 5
print time.strftime( ISOTIMEFORMAT, time.localtime(begin))
print time.strftime( ISOTIMEFORMAT, time.localtime(end))
