import math
INT_BITS=32
def carry(n):
    if len(hex(n))>10:
        return hex(n)[3:]
    else:
        return hex(n)[2:]
def boolfunc(s):
    l=[]
    for i in range(len(s)):
        if s[i]=="(":
            continue
        elif s[i]==")":
            continue
        else:
            l.append(s[i])
    return l
def leftRotate(n,d):
    return (n<<d)|(n>>(INT_BITS-d))
def rightRotate(n,d):
    return (n>>d)|(n<<(INT_BITS-d)) & 0xFFFFFFFF
msg=input("Enter the message:")
bval=input("Enter the Boolean funtion:")
print(boolfunc(bval))
round1addr=[]
address=[]
print("Enter the address:")
for i in range(5):
    a=int(input(),16)
    address.append(a)
print(address)
#Step 1
print("----------STEP 1----------")
AND1=address[1] and address[2]
NOT1=not(address[1])
AND2=NOT1 and address[3]
OR1= AND1 or AND2
print("Result of step 1:",hex(OR1)[2:])
#Step2
print("----------STEP 2----------")
ADD1=OR1+address[4]
ADDfinal=carry(ADD1)
print("The result of step 2 is:",ADDfinal)
l=[]
#Step 3
print("----------STEP 3----------")
#Conversion of Hexadecimal to Binary
addrA=int(address[0])
addrA_final=format(addrA,'032b')
l.append(addrA_final[5:])
for i in range(5):
    l.append(addrA_final[i])
l_final="".join(l)
#conversion of string into binary:
bin_value=int(l_final,base=2)
print("The result of Left Circular Shift is:",bin_value)
addrhex=hex(bin_value)
print("The hexadecimal equivalent of the shifted binary number is:",addrhex)
#STEP 4:
print("----------STEP 4----------")
ADD2=int(addrhex,base =16)+ADD1
#print(hex(ADD2))
#ADD2_hexval=int(ADD2,base=16)
ADD2final=carry(ADD2)
print("The result of step 4 is:",ADD2final)
#STEP 5:
print("----------STEP 5----------")
#String to ASCII Values
print("Given Message:",msg)
ascii_values=[ord(char) for char in msg]
ascii_hex=[hex(i) for i in ascii_values]
ascii_hex2=[]
for i in ascii_hex:
    i=i[2:]#removing the preceeding 0*
    ascii_hex2.append(i)
ascii_final="".join(ascii_hex2)#Combining the list values
ascii_intval=int(ascii_final,base=16)#conversion of string to hexadecimal
ascii_hexval=hex(ascii_intval)
print("Hexadecimal equivalent of ",msg,"is:",ascii_hexval)
#STEP 5:
print("----------STEP 6----------")
ADD3=int(ascii_hexval,base=16)+ADD2
#ADD3=int(ADD3,base=16)
ADD3_final=carry(ADD3)
print("the result of step 5 is :",ADD3_final)
#STEP 6
print("----------STEP 7----------")
K1=(math.sqrt(2)*(2**30))
K1=int(K1)
K1_str=hex(K1)
K1_hex=int(K1_str,base=16)
ADD4=K1_hex+ADD3
ADD4_final=carry(ADD4)
print("The new address A1 is:",ADD4_final)
a=leftRotate(int(address[0]),5)
print("The new address 1 is:",hex(a)[2:])
b=leftRotate(int(address[1]),30)
print("The new Address C1 is :",hex(b)[2:])
print("The new Address D1 is:",hex(address[2]))
print("The new address E1 is:",hex(address[3]))



