import socket
s = socket.socket()
s.bind(("",12345))
s.listen(10)
c,a = s.accept()
y = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
w = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
def encryption(pt,key):
    ct = "m"
    for i in range(len(pt)):
        #ENcryption ==> C=P+K mod m
        '''e = 5 +6 =11 %26 =11 
        y[11]= m'''
        ct += y[(y.index(pt[i])+key)%26]
    print(ct," => ",ct)
def decryption(ct,key):
    s = ""
    for i in range(len(ct)):
        #Decryption ==> P=C-K mod m
        '''i =10 -8 '''
        s += y[((y.index(ct[i])-key)+26)%26]
    print(ct," => ",s)
def bruteForceAttack(ct):
    for i in range(26):
        s = ""
        for j in range(len(ct)):
            s += y[((y.index(ct[j])-i)+26)%26]
        print(i," => ",s)
def frequencAnalysisAttack(ct):
    l1,l2 = [],[]
    for i in ct:
        if(i not in l1):
            l1.append(i)
    print(l1)
    l1.sort(reverse = True)
    print(l1)
    for i in l1:
        l2.append(l1.count(i))
    print(l2)
    for i in w:
        for j in l1:
            s = ""
            print(i," ",j)
            key = ((y.index(j)-y.index(i))+26)%26
            for k in range(len(ct)):
                s += y[((y.index(ct[k])-key)+26)%26]
            print("Encrypted plain text : ",s)
            c = input("\nIs this the plain text that you expected[Y/N]?")
            if(c == "Y"):
                break    
        if(c == "Y"):
            break


'''def freq(ct,pt):
    l1,l2=[]
    for i in ct:
        if i in l1:
            count[i]=count[i]+1
        else
            count[i]=1'''


while(True):
    x = (c.recv(1024).decode("utf8")).split(":")
    '''p=ebby
             key=6
             s.send(bytes("1" : "ebby" : "6") '''
    '''list =[1,2,3]
    posi ---> 0, 1 ,2'''
    choice = int(x[0])
    if(choice == 1):
        pt,key = x[1],int(x[2])
        encryption(pt,key)
    elif(choice == 2):
        ct,key = x[1],int(x[2])
        decryption(ct,key)
    elif(choice == 3):
        ct = x[1]
        bruteForceAttack(ct)
    elif(choice == 4):
        ct = x[1]
        frequencAnalysisAttack(ct)

