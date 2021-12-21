import numpy as np
import sympy as sp
alpha="abcdefghijklmnopqrstuvwxyz"
def numencoding(text,ord):
    l=[]
    for i in text:
        m=alpha.index(i)
        l.append(m)
    return np.array(l).astype(int)
def multiply(one,two,ord):
    mul=[]
    for i in range(ord):
        for j in range(ord):
            mul+=one[i][j]*two[i][j]
    return mul
    #return np.matmul(numen, matkey).astype(int) % 26
print("HILL CIPHER")
pt=input("Enter the text :")
ord=int(input("Enter order of matrix"))
element=[]
for i in range(ord*ord):
    element+=input("Enter the key element value : ")
matkey=np.array(element).astype(int)%26
print(matkey)
numen=numencoding(pt,ord)
print(numen)
mul=multiply(numen,matkey,ord)
print("multiplication : ",mul)