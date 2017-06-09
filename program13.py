#Write a Python program to combine each line from first file with the corresponding line in second file
fo=open("file1.txt","r")
fo1=open("file2.txt","r")
for line1, line2 in zip(fo, fo1):
  print(line1+line2)
  
  
  '''Output
   python program13.py
   astha jain 
   Hello
   
   afd
   astha
   
   eg
   here
  '''

 
