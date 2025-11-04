numbers =[-10,20,-30,40,0,15,-5]
positive_numbers = [num for num in numbers if num> 0]
print("positive numbers:",positive_numbers)
N =[1,2,3,4,5]
squares= [n**2 for n in N]
print("squares of N numbers:",squares)
word="beautiful"
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("vowels in the word",vowels)
word2="computer"
ordinal_values=[ord(ch) for ch in word2]
print("ordinal values of each character:",ordinal_values)
