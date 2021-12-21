import socket
s = socket.socket()
s.connect(("127.0.0.1",12345))
print("****    CAESAR CIPHER    ****")
print("\nEnter\n\t1) To Encryption\n\t2) To Decryption\n\t3) To implement Brute Force Attack\n\t4) To implement Frequency Analysis Attack")
n = int(input("Enter your choice('0' to EXIT) :"))
while(n != 0):
    if(n == 1):
        pt = input("Enter the plain text: ")
        key = int(input("Enter the key value: "))
        s.send(bytes(str(n)+":"+pt+":"+str(key),encoding='utf8'))
        '''p=ebby
           key=6
           s.send(bytes("1" : "ebby" : "6") '''
    elif(n == 2):
        ct = input("Enter the cipher text: ")
        key = int(input("Enter the key value: "))
        s.send(bytes(str(n)+":"+ct+":"+str(key),encoding='utf8'))
    elif(n == 3):
        ct = input("Enter the cipher text: ")
        s.send(bytes(str(n)+":"+ct,encoding='utf8'))
    elif(n == 4):
        ct = input("Enter the cipher text: ")
        s.send(bytes(str(n)+":"+ct,encoding="utf8"))
    n = int(input("Enter your choice('0' to EXIT) :"))



'''Caesar cipher
p
c
key
encry ---> c=p+k mod m   i/o : p,key
decry ---> p=c-k mod m   i/o : c,key
brute ---> k=c-p mod m   i/o : p,c
freq  ---> k=c-p mod m'''





    
