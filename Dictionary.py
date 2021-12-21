alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d={}
for i in alphabet:
    for j in alphabet:
        s=i+j
        d[hash(s)]=s
choice = int(input("Enter 1-Password to hash conversion     2-Crack password using hash value   0-Exit : "))
while(choice!=0):
    if(choice==1):
        password=str(input("Enter a password : "))
        h = hash(password)
        print("Hash value of password : ",h)
    if(choice==2):
        h=int(input("Enter hash value : "))
        print("Password : ",d[h])
    choice = int(input("Enter 1-Password to hash conversion     2-Crack password using hash value   0-Exit : "))