import re

book1=open("Book1.txt",'r')
book2=open("Book2.txt",'r')
book3=open("Book3.txt",'r')

line=book1.read()
line=book2.read()
line=book3.read()
word=line.strip(" ")
nn=word.split()
longest_word =  max(word, key=len)
print (longest_word)
