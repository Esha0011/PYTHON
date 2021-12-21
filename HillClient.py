import socket
s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
print("* HILL CIPHER OPERATIONS *\n")
print("Enter...\n\t1) To Encryption\n\n\t2) To Decryption\n\n\t3) Known plain text and cipher text attack\n")
print("\nEnter your choice('0' to EXIT) :- ", end="")
choice = int(input())
while (choice != 0):
    flag = 0
    # ENCRYPTION
    if (choice == 1):
        print("\n        === ENCRYPTION ===  \n\nEnter the plain text to encrypt   :   ", end="")
        s1 = input()
        print("\nEnter the order of the key matrix :   ", end="")
        order = int(input())
        km = []
        for i in range(order):
            l1 = []
            l1 = list(map(int, input().split()))
            if (len(l1) != order):
                flag = 1
                print("A row should contain ", order, " elements, Try again!")
                break
            km.append(l1)
        if (flag == 0):
            s.send(bytes(s1 + ":" + str(order) + ":" + " ".join(
                str(km[i][j]) for i in range(order) for j in range(order)) + ":" + str(choice), encoding='utf8'))
            print("\nDecrypted text of ", "'", s1, "'", "   ==>  ", s.recv(1024).decode("utf-8"))

    # DECRYPTION
    elif (choice == 2):
        print("\n        === DECRYPTION ===  \n\nEnter the cipher text to decrypt  :   ", end="")
        s1 = input()
        print("\nEnter the order of the key matrix :   ", end="")
        order = int(input())
        km = []
        for i in range(order):
            l1 = []
            l1 = list(map(int, input().split()))
            if (len(l1) != order):
                flag = 1
                print("A row should contain ", order, " elements, Try again!")
                break
            km.append(l1)
        if (flag == 0):
            s.send(bytes(s1 + ":" + str(order) + ":" + " ".join(
                str(km[i][j]) for i in range(order) for j in range(order)) + ":" + str(choice), encoding='utf8'))
            x = s.recv(1024).decode("utf-8")
            if (len(x) > 1):
                print("\nDecrypted text of ", "'", s1, "'", "   ==>  ", x)
            else:
                print("\nDecryption is not possible...")

    # Known plain text and cipher text attack
    elif (choice == 3):
        print("\n\n        === KNOWN PLAIN TEXT CIPHER TEXT ATTACK ===\n\nEnter the plain text    : ", end="")
        s2 = input()
        print("\nEnter the cipher text   : ", end="")
        s1 = input()
        print("\nEnter order of the key  : ", end="")
        order = int(input())
        s.send(bytes(s1 + ":" + s2 + ":" + str(order) + ":" + str(choice), encoding='utf8'))
        print("\nDecryption key :  ")
        l = (s.recv(1024).decode("utf-8")).split(" ")
        k = 0
        if (len(l) > 1):
            for i in range(order * order):
                if (k % order == 0):
                    print()
                print(l[k], end=" ")
                k += 1
        else:
            print("\nKnown plain text and cipher text attack is not possible...")
    else:
        print("\nOops! you have entered invalid choice...")
    print("\nEnter your choice('0' to EXIT) :- ", end="")
    choice = int(input())





