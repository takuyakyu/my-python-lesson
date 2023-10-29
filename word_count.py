file_path = "sample.txt"

with open(file_path, "r") as file:
    text = file.read()
    
words = text.split()

word_count = {}
for word in words:
    word = word.strip('.,?!').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    
print("単語の出現確率:")
for word, count in word_count.items():
    print(f"{word}: {count}")