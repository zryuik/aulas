"""teste = []
teste.append("Yure")
teste.append(24)

#print(teste)

galera = []
galera.append(teste[:])

#print(galera)

teste[0] = "Maria"
teste[1] = 22

galera.append(teste[:])

print(teste)"""


"""galera= [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]

for p in galera:
    #print(p[1])
    #print(p[0])
    print(f"{p[0]} tem {p[1]} anos de idade. ")"""

totmai = totmen = 0
galera = []
dados = []
for c in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade")