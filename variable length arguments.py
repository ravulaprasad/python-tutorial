def sum(*args):
    r=0
    for i in args:
        r+=i
    print(r)
#calling block
sum()
sum(-10,20,30)
sum(1.5,9,7,True)