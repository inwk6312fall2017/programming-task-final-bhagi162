book1=open("Book1.txt",'r')
book2=open("Book2.txt",'r')
book3=open("Book3.txt",'r')

line=book1.read()
line=book2.read()
line=book3.read()
word=line.strip(" " or '.')
nn=word.split()
longest = 0
for i in nn:
    if len(i) > longest:
        longest = len(i)
        longest_word = i
 
print( "The longest word is %s" % longest_word )
