f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt", "r")
data = f.read(5)
print(data)
print(type(data))
f.close()

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
f.close()

#  write mode

f = open("demo.txt", "a")
write = f.write("\nafter that i have to do my resume to make sure that i can take my jobs")
print(write)
f.close()

#with mode

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

#deleting file

import os

os.remove("sample.txt")

f = open("practice.txt", "w+")
write = f.write("hi everyone\n we are learning file i/o\n using java.\n i like programing in java")
print(write)
f.close()

#practice question 2

with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("java","python")
print(new_data)

#practice question 3

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word)!= -1):
        print("found")
    else:
        print("not found")    

