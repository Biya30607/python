import math
start=int(input("Enter start of range:"))
end=int(input("Enter end of range:"))
result=[]
for num in range(start,end+1):
    root=int (math.sqrt(num))
    if root*root==num:
        digits=str(num)
        if all(int(d)%2==0 for d in digits):
            result.append(num)
            print("Four-digit numbers with all even digits and perfect squares are:")
            print(result)
