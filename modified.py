string= input("enter a string:")
if len (string)<2:
    modified_string=string
else:
    modified_string=string[-1]+string[1:-1]+string[0]
    print("modified string:",modified_string)
