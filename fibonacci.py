n=int(input("Enter the number of terms:"))
a,b=0,1
if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibonacci sequence up to",n,"term:")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(a,end="")
        a,b=b, a+b
