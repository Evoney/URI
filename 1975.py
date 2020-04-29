P,A,R = input().split(" ")
P = int(P)
A = int(A)
R = int(R)
resp = []
names = []
resn = []
namesp = []
maiores = []
respmaiores = []

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

while ( P != 0 or A != 0 or R != 0):
    for i in range(P):
        resp.append(input())
    for i in range(A):
        names.append(input())
        for j in range(R):
            resn.append(input())
    for i in range(A):
        for j in range(((i+1)*R)-R,(i+1)*R):
            if (resp.count(resn[j]) == 1 and respmaiores.count(resn[j]) == 0 and namesp.count(names[i]) == 0):
                namesp.append(names[i])
                respmaiores.append(resn[j])
        respmaiores = []
        
    P,A,R = input().split(" ")
    P = int(P)
    A = int(A)
    R = int(R)

    if (len(namesp) > 1):
        maiores.append(namesp[0])  
        for i in namesp:
            if (namesp.count(i) > namesp.count(maiores[0])):
                maiores = []
                maiores.append(i)
            if (namesp.count(i) == namesp.count(maiores[0])):
                  maiores.append(i)
        maiores = remove_repetidos(maiores)
        maiores.sort()
        print(*maiores, sep=", ")
    else:
        print(*namesp)
