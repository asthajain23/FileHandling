#Write a Python program to get the file size of a plain file
import os
fo=open("file7.txt","w+")
fo.write("asthajain\nbye")
fo.close()
str= os.stat("file7.txt")
print str.st_size



'''Output
python program10.py
13
'''
