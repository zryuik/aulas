lanche = ["hamburger","suco","pizza","pudim"]
print(lanche)
lanche[3] = "picole"
print(lanche)
lanche.append("sorvete")
print(lanche)
lanche.remove("sorvete") #remove o indice e refaz os indices
print(lanche)
print(sorted(lanche)) #deixa os indices em ordem
lanche.pop(3) #remove o ultimo indice
print(lanche)
if "hamburger" in lanche:
    lanche.remove("hamburger")
    print(lanche)

valores = list(range(4,11))
print(valores)

val = list(range(4, 11, 2))
print(val)
for v in val:
    print(v)

valoress = [8,2,5,4,9,3,9]
print(valoress)
valoress.sort()
print(valoress)
valores.sort(reverse=True) #metodo sort de outra forma

print(len(valores)) #metodo len ultilizado para saber o tamanho da lista

num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f"Essa lista tem {len(num)} elementos. ")
num.insert(2, 0) #insere valor na posição que você escolhe
print(num)