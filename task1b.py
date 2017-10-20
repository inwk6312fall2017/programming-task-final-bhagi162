import re

book1=open("Book1.txt",'r')
book2=open("Book2.txt",'r')
book3=open("Book3.txt",'r')

line=book1.read()
line=book2.read()
line=book3.read()
word=line.strip(" ")
nn=word.split()
longest_word = ''
for i in word:
  if len(i) > len(longest_word)
    longest_word = word
print (longest_word)



