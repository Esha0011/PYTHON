import socket
s=socket.socket()
port=12345
s.connect(('localhost',port))
choice = int(input("Enter 1-Encryption 2-Decryption 3-Known plain text cipher text attack 0-exit: "))
while(choice!=0):
 s.send(choice.to_bytes(2,'big'))
 if(choice==1):
    text=str(input("Enter the text for encryption : "))
    s.send(bytes(text, encoding='utf8'))
    size = int(input("Enter the order of key matrix : "))
    s.send(size.to_bytes(2,'big'))
    for i in range(size):
        row=str(input())
        s.send(bytes(row, encoding='utf8'))
if(choice==2):
    text=str(input("Enter the text for decryption : "))
    s.send(bytes(text, encoding='utf8'))
    size = int(input("Enter the order of key matrix : "))
    s.send(size.to_bytes(2,'big'))
    for i in range(size):
        row=str(input())
        s.send(bytes(row, encoding='utf8'))
 if(choice==3):
 plain_text=str(input("Enter the plain text : "))
 s.send(bytes(plain_text, encoding='utf8'))
 cipher_text=str(input("Enter the cipher text : "))
 s.send(bytes(cipher_text, encoding='utf8'))

 ans=s.recv(1024)
 print(ans.decode())
 choice = int(input("Enter 1-Encryption 2-Decryption 3-Known plain text ciphertext attack 0-exit: "))
s.close()