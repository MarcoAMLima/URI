A, B, C, D = map(int, input().split())

auxAB = A + B
auxCD = C + D

if (B > C)and(D > A)and(auxCD > auxAB)and(C > 0)and(D > 0)and((A % 2) == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
