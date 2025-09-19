from math import sqrt, floor
num = int(input('digite um número: '))
raiz = sqrt(num)
print(f"A raiz de {num} é igual a {raiz:.2f} arrendodada para baixo {floor(raiz)}")
