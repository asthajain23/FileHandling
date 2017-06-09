# Write a Python program to read a file line by line and store it into a list
import io
li=[]
fo=open("a.txt","w+")
fo.write("\nHello\nastha\nhere")
fo=open("a.txt","r")
i=fo.readlines()
li.append(i)
print i


'''Output
 python program5.py
 ['\n', 'Hello\n', 'astha\n', 'here']
'''
