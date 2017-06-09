#Write a Python program to read a file line by line store it into an array
import io
array=[]
fo=open("a.txt","w+")
fo.write("Hello astha here")
fo.seek(0,0)
with open("a.txt","r") as f:
 for i in f:
        print(array.append(i))



'''Output
'''
