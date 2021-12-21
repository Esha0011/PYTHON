import  math

def euliersTotient(p,q):
	return (p-1)*(q-1)

def euclidean(a,b): 
    if(b == 0): return a
    l.append(math.floor(a/b)) 
    return euclidean(b,a%b)

def multiplicativeInverse(a,b): 
    if(euclidean(a,b) == 1):
        t1,t2,i = 0,1,0
        while(abs(t2) != max(a,b) and i<len(l)):
            if(i<len(l)): t = t1 - (t2 * l[i]) 
            t1,t2,i = t2,t,i+1

        if(t1<0): 
            t1 = t1+a 
        return t1
    else: return 0


print("Enter...\n\t1) To Key Generation\n\t2) To Encrytion\n\t3) To Decryption\n\t4) To EXIT")
n1 = int(input("\nEnter your choice(4 to EXIT) : "))
while(n1 != 4):
    a = "abcdefghijklmnopqrstuvwxyz"
    if(n1 == 1):
        p = int(input("\nEnter the first prime number : "))
        q = int(input("\nEnter the second prime number: "))
        n = p*q
        num = euliersTotient(p,q)  #gcd of tot and e =1
        while(True):
            e = int(input("\nEnter the value of e : "))  #'''gcd(e(x),tot)=1'''
            l = []
            d = multiplicativeInverse(max(e,num),min(e,num)) #d=e^-1 mod tot(n)
            if(d != 0): break
        print("\nValue of 'n'\t\t: ",n,"\nValue of phi of n\t: ",num,"\nValue of 'd'\t\t: ",d,"\nPublic key(e,n) \t: (",e,",",n,")","\nPrivate key(d,n) \t: (",d,",",n,")")
    if(n1 == 2):
        pt = input("\nEnter the plain text \t: ")
        '''Ebby = E B B Y'''
        e = int(input("\nEnter 'e' value \t:  "))
        n = int(input("\nEnter 'n' value \t:  "))
        for k in pt:
            i = a.index(k)
            prod = math.floor(pow(i,e,n)%n)
            ''' i^e mod n = 4^3 mod 11'''
            print(k," = ",prod)
            print("The element is " , chr(97+prod))
            '''ord----> if given e=5
               chr----> ascii char kudukum
               chr(97+value)----> gives alpha equivalent'''

    if(n1 == 3):
        s = ""
        ct =input("\nEnter the Plain text values  : ").split()
        p = int(input("\nEnter the first prime number : "))
        q = int(input("\nEnter the second prime number: "))
        n = p*q
        num = euliersTotient(p,q)
        e = int(input("\nEnter the value of e         : "))
        l = []
        d = multiplicativeInverse(max(e,num),min(e,num))
        for i in ct:
             prod = math.floor(pow(i,d,n)%n) #P=i^d mod n
             print(i,"\t\t\t: ",prod)
             s += str(prod)
    n1 = int(input("\nEnter your choice(4 to EXIT) : "))


    ''''''