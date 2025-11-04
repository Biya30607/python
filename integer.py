numbers=list(map(int,input("Enter integers seperated by spaces:").split()))
result=["over"if num>100 else num for num in numbers]
print("\n Final list:",result)
