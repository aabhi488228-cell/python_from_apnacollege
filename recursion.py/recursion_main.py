def show(n):
    print(n)

show(5)  
# recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(6)

def fact(n):
    if(n == 1 or n ==0):
        return 1
    else:
        return fact(n-1) * n
print(fact(5))