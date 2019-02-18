#fibonacci sequence
def fibo(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
x=150
if x<=0:
    print("wrong number")
else:
    for i in range(x):
        print(fibo(i),end=" ")
