#Write a Python program to count the frequency of words in a file
fo=open("file6.txt","w+")
fo.write("Hello astha here hello bye i am working astha !")
fo.close()
fo=open("file6.txt","r+")
wordcount={}
for word in fo.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

print wordcount


'''Output
python program9.py
{'!': 1, 'working': 1, 'astha': 2, 'am': 1, 'here': 1, 'hello': 1, 'i': 1, 'bye': 1, 'Hello': 1}
'''
