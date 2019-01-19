def Outer():
    def Inner():
        return 'Technologies'
    return Inner
#calling block
another=Outer()
x=another()
print(x)