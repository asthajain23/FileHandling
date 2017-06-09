#Write a python program to find the longest words
def main ():
    text = raw_input("Please input a List of words to evaluate: ")
    longest = 0
    for words in text.split():
           if len(words) > longest:
                  longest = len(words)
    print ("The longest word is", words, "with lenght", longest)

main()



'''Output

python program8.py
Please input a List of words to evaluate: astha jain zensar cognizant companies byeeeee
('The longest word is', 'byeeeee', 'with lenght', 9)
'''
