C1, Q1, P1 = map(float, input().split(" "))
C2, Q2, P2 = map(float, input().split(" "))

V = (Q1 * P1) + (Q2 * P2)

print("VALOR A PAGAR: R$ {:.2f}".format(V))