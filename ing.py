
text = input("Enter a string: ")


if len(text) >= 3:
    if text.endswith("ing"):
        text += "ly"
    else:
        text += "ing"
else:
    text = text 

print("Result:", text)
