import string
import random
#Message to code
aa = input("Enter whether you want to 'code' or 'decode' :- ")
if aa == "code":
  x = input("Enter a message : ")
  y = x.split(" ")
  for i in range(0,len(y)):
    z = y[i]
    print(" ",end='')
    for t in range(0,3):
      r = random.choice(string.ascii_letters)
      print(r,end='')
    for j in range(0,len(y[i])):
      pass
    print(z[j],end='')
    for k in range (0,(len(y[i])-1)):
      s = z[k]
      print(s,end='')
    for m in range(0,3):
      r = random.choice(string.ascii_letters)
      print(r,end='')

# Code to message
elif aa == "decode":
  x=input("Enter the secret code:")
  y=x.split(" ")
  for i in range(0,len(y)):
    z = y[i]                      
    for j in range(4,(len(z)-3)): 
      print(z[j],end='')
    print(z[3],end=' ')
