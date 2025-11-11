#parâmetros opcionais

def soma(a=0,b=0,c=0):
    """
    Calcula a soma de até três números e retorna o resultado.

    Parâmetros:
        a (int | float, opcional): Primeiro número a ser somado. Padrão é 0.
        b (int | float, opcional): Segundo número a ser somado. Padrão é 0.
        c (int | float, opcional): Terceiro número a ser somado. Padrão é 0.

    Retorna:
        int | float: O resultado da soma entre os valores fornecidos.

    Exemplo:
        >>> soma(3, 2, 5)
        10
        >>> soma(4, 2)
        6
    """
    soma = a+b+c
    print(soma)

a = int(input(": "))
b = int(input(": "))
c = int(input(": "))
soma(a,b,c)