
import pprint
import re
import time

file = open('access.log','rb')
read = file.readlines()
start = time.time()
count = {}
for line in read:
    look = re.compile(r'(\d\d\d.)(\d\d\d\.)(\d\d\d.)(\d\d\d)')
    found = look.search(line)
   # if found not None:
    try:
        ip = found.group()
        count.setdefault(ip,0)
        count[ip] = count[ip] + 1
        #print count
    except:
        continue
end = time.time()
#pprint.pprint(count)
a=pprint.pformat(count)
print a
print "Total Time taken : %d" %(end-start)
