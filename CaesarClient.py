import socket
soc=socket.socket()
soc.connect("127.0.0.1",14567)

print("************ Welcome to Caesar Cipher **********")
flag=0
while(flag==0):
    print("Menu \n\t 1 - Encryption \n\t 2 - Decryption")
    choice=int(input("Enter your choice : (press 0 to exit) "))
    while(choice==0 or choice==1 or choice==2 or choice==3):
        if(choice==1):
            print("****ENCRYPTION****")
            pt=input("Enter the plain text : ")
            key=int(input("Enter the key : "))
            s.send(bytes(str(choice)+":"+pt+":"+str(key),encoding="utf8"))
        elif (choice == 2):
            print("****DECRYPTION****")
            ct = input("Enter the cipher text : ")
            key = int(input("Enter the key : "))
            s.send(bytes(str(choice) + ":" + ct + ":" + str(key), encoding="utf8"))
        else:
            print("Exiting system")

    print("Please enter a valid choice")
