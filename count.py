names=input("Enter first names separated by spaces:").split()
count_a=sum(name.lower().count('a')for name in names)
print("\nTotal occurences of 'a':",count_a)
