#Write a Python program to read a random line from a file
import random
fo=open("file2.txt","w+")
fo.write("Hello\nastha\nhere")
fo.close()
str = random.choice(open("file2.txt").readlines())
print str



'''Output
 python program14.py
 astha
'''
