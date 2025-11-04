list1=list(map(int,input("Enter integers for first list(separated by spaces):").split()))
list2=list(map(int,input("Enter integers for second list(separated by spaces):").split()))
print("\nList1:",list1)
print("List2:",list2)
if len(list1)==len(list2):
    print("\n(a)Both lists are of the same length.")
else:
     print("\n(a)Lists are of different lengths.")
if sum(list1)==sum(list2):
    print("\n(b)Both lists sum to the same value.")
else:
    print("\n(b)Lists do not to the same value.")
common_values=set(list1)&set(list2)
if common_values:
    print(f"(c)Common values in both lists:{list(common_values)}")
else:
    print(f"(c)No common valuesfound in both lists.")
    
