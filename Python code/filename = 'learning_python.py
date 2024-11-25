#tells the code which file it is supposed to open
file = "Documents/learningpython.txt"
#tells it just to read the file 
for i in range(3):
    print(open(file).read())
#to print all the lines in the file 
with open(file, 'r') as fin:
    for lines in fin:
        print(lines)

with open(file,'r') as fin:
     my_text = fin.readlines()

cleaned_text = []

for text in my_text:
    cleaned_text.append(text.rstrip("\n"))
print(cleaned_text)



This Python code has you create a file in your file explorer and write something in it and then open the file in python and print whats in the file. 
