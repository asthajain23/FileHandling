#Write a Python program to read a file line by line store it into a variable
import io
str=" "
fo=open("aaa.txt","w+")
fo.write("Hello astha here")
fo=open("aaa.txt","r")
str=fo.readlines()
print str


'''Output
python program6.py
['Hello astha here']
'''
