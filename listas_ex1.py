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
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numero 4") 