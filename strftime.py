from datetime import *
td=datetime.today()
mystr=td.strftime('%A,%b,%d,%Y,%H:%M %p')
print(mystr)
mystr2=td.strftime('Today is %j day of the year')
print(mystr2)