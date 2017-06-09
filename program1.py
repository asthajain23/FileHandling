#Write a Python program to read an entire text file and print its contents
import io
fo=open("abc.txt","w+")
fo.write("\nHello\nastha\nhere")
fo.close()
fo=open("abc.txt","r")
'''if fo.mode == 'r':
    contents =fo.read()
print (contents)'''
fl =fo.readlines()
for x in fl:
     print(x)
     
     
'''Output
Hello
astha
here
'''     
     
