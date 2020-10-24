X, Y = map(int, input().split())

lines = []
while ((X != 0) and (Y != 0)):
    line = "{} {}".format(X,Y)
    lines.append(line)
    X, Y = map(int, input().split())


for line in lines:

    parameters = line.split()

    D = parameters[0]
    N = parameters[1]

    
    newN = [digit for digit in N if (D != digit)]
    newN = "".join(newN)

    if(newN == ""):
        print(0)
    else: 
        print(int(newN))
