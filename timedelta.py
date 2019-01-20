from datetime import *
d1=date(year=2000,month=12,day=22)
d2=date(year=2017,month=1,day=12)
dlt=d2-d1
print('The diff b/w two dates in weeks:',dlt.days/7)
print('The diff b/w two dates in days:',dlt.days)

