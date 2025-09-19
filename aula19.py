# dados = {
#     "nome":"Pedro",
#     "idade": 25
#     }


    
# dados["sexo"] = "M"
# print(dados["nome"])
# #del(dados["idade"])
# print(dados)


# filme = {

#     "titulo":"Star Wars",
#     "ano":1977,
#     "diretor": "George Lucas"

# }

# print(filme)
# print(filme.values()) #mostra os valores
# print(filme.keys()) #mostra as chaves
# print(filme.items()) #mostra nome e chave


# for k,v in filme.items():
#     print(f"o {k} é {v}")

# print(f"O {dados["nome"]} tem {dados["idade"]} anos")



# brasil = []
# estado1 = {
#     "uf":"Rio De Janeiro",
#     "sigla":"RJ"
# }

# estado2 = {
#     "uf":"São Paulo",
# "sigla" : "SP"

# }

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil)
# print(brasil[0])
# print(brasil[1])
# print(brasil[0]["uf"])
# print(brasil[1]["uf"])
# print(brasil[0]["sigla"])
# print(brasil[1]["sigla"])

# estado = dict()
# brasil = list()

# for c in range(0,3):
#     estado["uf"] = str(input("Unidade Federativa: "))
#     estado["sigla"] = str(input("Sigla Federativa: "))   
#     brasil.append(estado.copy()) 
# for e in brasil:
#     for v in e.values():
#         print(v,end=" ")
#     print()

# print(brasil)