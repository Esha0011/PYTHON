import math 
import socket 
import random

s = socket.socket() 
s.connect(('127.0.0.1', 123 ))
def PrimitiveRoot(p): 
    print("\nPrimitive roots are :- ",end=" ")
    for j in range(2,p): 
        l = []
        for i in range(1,p): 
            x = (j**i)%p 
            if(x not in l):l.append(x)  
            else: break 
        if(len(set(l)) == p-1):  print(j,end=" ") 
def ModularExponentiation(a,b,c):  
    prod = 1
    for i in range(1,a+1): 
        prod = math.floor((prod*b)%c) 
    return prod 

def discreteLog(a,b,c):
    i = 1
    while(True):
        if(pow(b,i,c) == a):
            print("\nDiscrete log = ",i)
            break
        i += 1
		
print("Enter\n\t1) Secret key generation\n\t2) Discrete log\n\t3) Man in the middle")
n = int(input("\nEnter your choice(0 to EXIT):- "))

while(n!=0):
    s.send(bytes(str(n),encoding='utf8'))
    if(n == 1):
        print("\n***Secret Key Generation***")
        c1 = int(input("\nEnter User A's Confidential key: ")) 
        p1 = int(input("\nEnter Prime number : ")) 
        PrimitiveRoot(p1) 
        pr = int(input("\n\nEnter the primitive root: "))
        print("\nPrimtive root => ",pr) 
        ku1 = ModularExponentiation(c1,pr,p1) 
        print("\nPublic Key of User A => ",ku1) 
        s.send(bytes(str(ku1),encoding='utf8')) 
        num = int(s.recv(1024).decode("utf-8")) 
        kr1 = ModularExponentiation(c1,num,p1) 
        print("\n\nSecret Key => ",kr1) 
    elif(n == 2):
        print("\n***Discrete Log Generation***")
        a = int(input("\nEnter Y_a value          : "))
        b = int(input("\nEnter prime root value   : "))
        c = int(input("\nEnter prime number value : "))
        discreteLog(a,b,c)
    elif(n == 3):
        print("\n***Man In The Middle***")
        a = random.randint(1,20)
        print("\nFake secret number : ",a);
        p1 = int(input("\nEnter Prime number : ")) 
        PrimitiveRoot(p1) 
        pr = int(input("\n\nEnter the primitive root: "))
        ku1 = ModularExponentiation(a,pr,p1) 
        s.send(bytes(str(ku1),encoding='utf8')) 
        num = int(s.recv(1024).decode("utf-8")) 
        kr1 = ModularExponentiation(a,num,p1) 
        print("\n\nFake Secret Key => ",kr1)     
    n = int(input("\nEnter your choice(0 to EXIT):- "))
