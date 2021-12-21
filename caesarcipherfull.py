def Encryption(pt,key):
	str=""
	for i in pt:
		n=(Alpha.index(i)+key)%36
		str+=Alpha[n]
	return str

def Decryption(ct,key):
	str=""
	for k in ct:
		n=(Alpha.index(k)-key)%36
		str+=Alpha[n]
	return str
def BruteForce(ct):
	for i in range(0,35):
		str=""
		for j in ct:
			n=(Alpha.index(j)-i)%36
			str+=Alpha[n]
		print(str," is the plaintext when key = ", i)



print("WELCOME TO CAESAR CIPHER")
choice=int(input("Enter choice \n\t 1-Encryption \n\t 2-Decryption \n\t 3-BruteForce\n"))
Alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
while(True):
	if(choice==1):
		print("*****Encryption****")
		pt=input("Enter Plaintext : ")
		key=int(input("Enter Key : "))
		Encrypt=Encryption(pt,key)
		print(Encrypt, " is the encrypted text ")

	elif(choice==2):
		print("****Decryption****")
		ct=input("Enter Ciphertext :")
		key=int(input("Enter Key :"))
		Decrypt=Decryption(ct,key)
		print(Decrypt, " is the decrypted text")

	elif(choice==3):
		print("****Brute Force****")
		ct=input("Enter Ciphertext :")
		BruteForce(ct)
		print("All possibilities of plaintext are found")

	choice = int(input("Enter choice \n\t 1-Encryption \n\t 2-Decryption \n\t 3-BruteForce\n"))
