#Write a Python program to append text to a file and display the text
import io
fo=open("abcde.txt","w+")
fo.write("\nHello\nastha\nhere")
fo.close()
fo=open("abcde.txt","a")
fo.write("this is the appended content\nbye")
#fo.read("abcde.txt")
fo=open("abcde.txt","r")
str=fo.read()
print str
fo.close()


'''Output
python program3.py
Hello
astha
herethis is the appended content
bye
'''
