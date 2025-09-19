# Solicita o valor original do produto
valor = float(input("Digite o valor do produto: R$ "))

# Solicita o percentual de desconto
desconto = float(input("Digite o percentual de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = valor * (desconto / 100)

# Calcula o valor final com desconto
valor_final = valor - valor_desconto

# Exibe os resultados
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor com desconto: R$ {valor_final:.2f}")
