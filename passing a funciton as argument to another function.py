def fun1(fun):
    return 'Hello' + ' ' + fun()
def fun2():
    return 'David'
#calling block
mystr=fun1(fun2)
print(mystr)