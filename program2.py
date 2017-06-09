#Write a Python program to read first n lines of a file and print these lines
try:
    file=open("ab.txt","w+")
    file.write("Hello\nastha\nhere i work in zensar\ni am software engineer\n i live in pune\n i earn a good salary\n bye")
    line=int(input("Enter number of lines to be read:"))
    with open("ab.txt", "r") as file:
        for i in range(line):
                print file.next()
except StopIteration:
    print ("sorry number overflow")
    
    
    
    '''Output
    python program2.py
    Enter number of lines to be read:3
    Hello
    astha
    here i work in zensar
    '''
