import string

PUNCTUATION = string.punctuation

comments = []

filename = input("Podaj nazwę pliku:")
with open(filename) as stream:
    text = stream.read()

text = text.lower()
texts = text.split("\n")

for text in texts:
    for char in text:
        if char in PUNCTUATION:
            text = text.replace(char,"")
    text = text.split()
    comments.append(text)

pattern = input("Ile razy w pliku powtarza się słowo: ", )
pattern = pattern.lower()

words_count = 0
for word in comments:
    if pattern in word:
        words_count += 1

print("Słowo ", pattern ,"w podanym pliku pojawia się", words_count, "razy")

