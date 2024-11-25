file = "Documents/learningpython.txt"

for i in range(3):
    print(open(file).read())

with open(file, 'r') as fin:
    for lines in fin:
        print(lines)

with open(file,'r') as fin:
     my_text = fin.readlines()

cleaned_text = []

for text in my_text:
    cleaned_text.append(text.rstrip("\n"))
print(cleaned_text)