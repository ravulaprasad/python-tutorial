def Outer():
    def Inner():
        return 'Technologies'
    return 'Sathya' + ' ' + Inner()
#calling block
mystr=Outer()
print(mystr)