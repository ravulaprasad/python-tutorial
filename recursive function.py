def Factorial(n):
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
#calling block
x=Factorial(int(input()))
print(x)