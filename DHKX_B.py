import socket 
import math 
import random
s = socket.socket() 
s.bind(('', 123))
s.listen(10) 
c, addr = s.accept() 
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
def modul(a,b,c):
    prod=1
    prod=math.floor((a**b)%c)
    return prod
def discreteLog(a,b,c):
    i = 1
    while(true):
        if(pow(b,i,c) == a):
            print("Discrete log = ",i)
        i += 1
while(True):
    choice = int(c.recv(1024).decode("utf-8"))
    if(choice == 1):
        print("\n***Secret Key Generation***")
        c2 = int(input("\nEnter User B's Confidential key: ")) 
        p1 = int(input("\nEnter Prime number : ")) 
        PrimitiveRoot(p1) 
        pr = int(input("\n\nEnter the primitive root: "))
        nummo=modul(pr,c2,p1)
        print(nummo)
        ku2 = ModularExponentiation(c2,pr,p1) 
        print("\nPublic Key of User B => ",ku2) 
        num = int(c.recv(1024).decode("utf-8"))

        kr2 = ModularExponentiation(c2,num,p1) 
        print("\nSecret Key => ",kr2)
        c.send(bytes(str(ku2),encoding='utf8'))
    elif(choice == 3):
        print("\n***Man in the middle***")
        a = random.randint(1,20)
        print("\nFake secret number : ",a);
        p1 = int(input("\nEnter Prime number : ")) 
        PrimitiveRoot(p1) 
        pr = int(input("\n\nEnter the primitive root: "))
        ku2 = ModularExponentiation(a,pr,p1) 
        num = int(c.recv(1024).decode("utf-8"))
        kr2 = ModularExponentiation(a,num,p1) 
        print("\nFake Secret Key => ",kr2)
        c.send(bytes(str(ku2),encoding='utf8'))