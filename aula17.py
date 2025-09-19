#manipulação de listas
lanche = ['hamburguer', 'suco','pizza', 'pudim'] 


lanche.append('biscoito') #insere um elemento no final da lista
print(lanche)

lanche.insert(0, 'cachorro quente')#insere um elemento a lista na posição que voce deseja
print(lanche)


del lanche[3] #remove o item pela chavve
lanche.pop(3) #remove pela chave ou se ultilizas lanche.pop() remove o ultimo elemento
print(lanche)
lanche.remove('pizza') # remove o indice que voce quer
print(lanche)

sorted(lanche)
print(lanche)
if 'sopa' in lanche:
    lanche.remove('sopa')
else:
    print('sopa e nao é janta')