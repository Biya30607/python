text=input("Enter a line of text:")
words=text.lower().split()
word_count={word:words.count(word)for word in words}
print("\nWord occurences:")
for word,count in word_count.items():
    print(f"{word}:{count}")
