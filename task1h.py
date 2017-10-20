import string
x=string.punctuation

book1=open("Book1.txt",'r')
book2=open("Book2.txt",'r')
book3=open("Book3.txt",'r')

line=book1.read()
line=book2.read()
line=book3.read()
for i in line:
    b=i.split()
c=b.strip(x)
print(c)
