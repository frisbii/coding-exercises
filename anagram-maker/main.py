import random

response = input("What would you like to anagram-ize?")
split = [c for c in str(response)]
new = []
length = len(split)

for i in range(len(split)):
    letter = random.choice(split)
    split.remove(letter)
    new.append(letter)

string = ""
string.join(new)
print(string)
