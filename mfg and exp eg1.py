from datetime import *
d,m,y=[int(x) for x in input('enter MFG data(dd/mm/yyyy):').split('/')]
date1=date(day=d,month=m,year=y)
d1,m1,y1=[int(x) for x in input('enter Exp date(dd/mm/yyyy):').split('/')]
date2=date(day=d1,month=m1,year=y1)
date3=date.today()
if date2>date3:
    print('Medicine not expired')
elif date2<date3:
    print('Medicine expired')
else:
    print('Medicine will expire today')