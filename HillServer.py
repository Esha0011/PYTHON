import socket
import math

s = socket.socket()
s.bind(('', 12345))
s.listen(10)
c, addr = s.accept()


def keyMatrix(n, key):
    l1 = []
    k = 0
    for i in range(n):
        l = []
        for j in range(n):
            l.append(int(key[k]))
            k += 1
        l1.append(l)
    return l1


def textToMatrix(n, text):
    l2 = []
    for i in range(n):
        l = []
        for j in range(len(text)):
            if (j % n == i): l.append(text[j])
        l2.append(l)
    return l2


def matProcess(n, l2):
    for i in l2[1:n + 1]:
        k = len(l2[0]) - len(i)
        if (k != 0):
            i.extend(k * "x")
    return l2


def numericEncoding(text, order):
    l2 = textToMatrix(order, text)
    l2 = matProcess(order, l2)
    a1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(l2)):
        for j in range(len(l2[0])):
            l2[i][j] = a1.index(l2[i][j].lower())
    return l2


def matMul(key, l2, p, r, s, m):
    op = [[0 for j in range(s)] for i in range(p)]
    for i in range(p):
        for j in range(s):
            for k in range(r):
                op[i][j] += key[i][k] * l2[k][j]
                op[i][j] = math.floor(op[i][j] % m)
    return op


def characterEncoding(l3, p, q):
    a1 = "abcdefghijklmnopqrstuvwxyz"
    for i in range(p):
        for j in range(q):
            l3[i][j] = a1[l3[i][j]]
    return l3


def determinant(l1, order, m):
    if (order == 2):
        det = (l1[0][0] * l1[1][1]) - (l1[0][1] * l1[1][0])
        if (det < 0): det = -(math.floor(-(det) % 26)) + 26
        return (math.floor(det % 26))
    elif (order == 3):
        det = (l1[0][0] * ((l1[1][1] * l1[2][2]) - (l1[1][2] * l1[2][1]))) - (
                    l1[0][1] * ((l1[1][0] * l1[2][2]) - (l1[1][2] * l1[2][0]))) + (
                          l1[0][2] * ((l1[1][0] * l1[2][1]) - (l1[1][1] * l1[2][0])))
        if (det < 0): det = -(math.floor(-(det) % 26)) + 26
        return (math.floor(det % 26))


def euclidean(a, b):
    if (b == 0): return a
    l.append(math.floor(a / b))
    return euclidean(b, a % b)


def multiplicativeInverse(a, b):
    if (euclidean(a, b) == 1):
        t1, t2, i = 0, 1, 0
        while (abs(t2) != max(a, b)):
            if (i < len(l)): t = t1 - (t2 * l[i])
            t1, t2, i = t2, t, i + 1
        if (t1 < 0): t1 = t1 + a
        return t1
    else:
        return 0


def adjoint(l1, q, mod):
    if (q == 2):
        temp = l1[0][0]
        l1[0][0], l1[1][1] = l1[1][1], temp
        l1[0][1], l1[1][0] = -(l1[0][1]), -(l1[1][0])
        if (l1[0][1] < 0): l1[0][1] += mod
        if (l1[1][0] < 0): l1[1][0] += mod
        return l1
    elif (q == 3):
        ll = []
        for i in range(q):
            y = []
            for j in range(q):
                y.append(0)
            ll.append(y)
        ll[0][0], ll[0][1], ll[0][2] = +((l1[1][1] * l1[2][2]) - (l1[2][1] * l1[1][2])), -(
                    (l1[1][0] * l1[2][2]) - (l1[2][0] * l1[1][2])), +((l1[1][0] * l1[2][1]) - (l1[1][1] * l1[2][0]))
        ll[1][0], ll[1][1], ll[1][2] = -((l1[0][1] * l1[2][2]) - (l1[0][2] * l1[2][1])), +(
                    (l1[0][0] * l1[2][2]) - (l1[0][2] * l1[2][0])), -((l1[0][0] * l1[2][1]) - (l1[0][1] * l1[2][0]))
        ll[2][0], ll[2][1], ll[2][2] = +((l1[0][1] * l1[1][2]) - (l1[1][1] * l1[0][2])), -(
                    (l1[0][0] * l1[1][2]) - (l1[0][2] * l1[1][0])), +((l1[0][0] * l1[1][1]) - (l1[1][0] * l1[0][1]))
        for i in range(q):
            for j in range(q):
                if (ll[i][j] < 0): ll[i][j] = -(math.floor(-(ll[i][j]) % 26)) + 26
                l1[j][i] = ll[i][j] % mod
        return l1


def scalarMultiplication(scalar, l2, order, mod):
    for i in range(order):
        for j in range(order):
            l2[i][j] = (scalar * l2[i][j]) % mod
    return l2


while (True):
    print("\nWaiting for client...")
    s1 = (c.recv(1024).decode("utf-8")).split(":")
    if (int(s1[-1]) == 1 or int(s1[-1]) == 2):
        choice, text, order, key = int(s1[-1]), s1[0], int(s1[1]), s1[2].split()
    else:
        order = int(s1[2])
        pt = s1[1][0:(order * order)]
        ct = s1[0][0:(order * order)]
        choice = int(s1[-1])
    if (choice == 1):
        print("\nENCRYPTION STARTED!!!")
        l1 = keyMatrix(order, key)
        l2 = numericEncoding(text, order)
        l3 = matMul(l1, l2, order, len(l2), len(l2[0]), 26)
        l4 = characterEncoding(l3, len(l3), len(l3[0]))
        s2 = ""
        for j in range(len(l4[0])):
            for i in range(len(l4)):
                s2 += l4[i][j]
        c.send(bytes(s2, encoding='utf8'))
        print("\nENCRYPTION COMPLETED!!!")

    elif (choice == 2):
        print("\nDECRYPTION STARTED!!!")
        l = []
        l1 = keyMatrix(order, key)
        det = determinant(l1, order, 26)
        mi = multiplicativeInverse(max(det, 26), min(det, 26))
        if (mi != 0):
            l1 = adjoint(l1, order, 26)
            l1 = scalarMultiplication(mi, l1, order, 26)
            l3 = numericEncoding(text, order)
            l3 = matMul(l1, l3, order, len(l3), len(l3[0]), 26)
            l4 = characterEncoding(l3, len(l3), len(l3[0]))
            s2 = ""
            for j in range(len(l4[0])):
                for i in range(len(l4)):
                    s2 += l4[i][j]
            c.send(bytes(s2, encoding='utf8'))
            print("\nDECRYPTION COMPLETED!!!")
        else:
            print("Oops! Multiplicative inverse does not exist\nImpossible to decrypt...")
            c.send(bytes("0", encoding='utf8'))

    else:
        print("\nKNOWN PLAIN TEXT CIPHER TEXT ATTACK STARTED!!!")
        l = []
        s1, s2 = numericEncoding(pt, order), numericEncoding(ct, order)
        det = determinant(s2, order, 26)
        mi = multiplicativeInverse(max(det, 26), min(det, 26))
        if (mi != 0):
            s2 = adjoint(s2, order, 26)
            l1 = scalarMultiplication(mi, s2, order, 26)
            l3 = matMul(s1, l1, order, len(l1), len(l1[0]), 26)
            c.send(bytes(" ".join(str(l3[i][j]) for i in range(order) for j in range(order)), encoding='utf8'))
        else:
            print(
                "Oops! Multiplicative inverse does not exist\nImpossible to undergo known plain and cipher text attack...")
            c.send(bytes("0", encoding='utf8'))
        print("\nKNOWN PLAIN TEXT CIPHER TEXT ATTACK TERMINATED!!!")
c.close()