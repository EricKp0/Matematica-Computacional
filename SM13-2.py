def encontrar_idades(homem1, homem2, mulher1, mulher2):
    if homem1 > homem2:
        homem_mais_velho = homem1
        homem_mais_novo = homem2
    else:
        homem_mais_velho = homem2
        homem_mais_novo = homem1

    if mulher1 > mulher2:
        mulher_mais_velha = mulher1
        mulher_mais_nova = mulher2
    else:
        mulher_mais_velha = mulher2
        mulher_mais_nova = mulher1

    return homem_mais_velho, homem_mais_novo, mulher_mais_velha, mulher_mais_nova

def calcular_soma_produto(homem_mais_velho, mulher_mais_nova, homem_mais_novo, mulher_mais_velha):
    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha
    return soma, produto

def validar_idade(idade):
    return isinstance(idade, int) and idade >= 0

try:
    homem1 = int(input("Digite a idade do homem 1: "))
    homem2 = int(input("Digite a idade do homem 2: "))
    mulher1 = int(input("Digite a idade da mulher 1: "))
    mulher2 = int(input("Digite a idade da mulher 2: "))
    
    homem_mais_velho, homem_mais_novo, mulher_mais_velha, mulher_mais_nova = encontrar_idades(homem1, homem2, mulher1, mulher2)

    soma, produto = calcular_soma_produto(homem_mais_velho, mulher_mais_nova, homem_mais_novo, mulher_mais_velha)

    print(f"A soma da idade do homem mais velho com a mulher mais nova é: {soma}")
    print(f"O produto da idade do homem mais novo com a mulher mais velha é: {produto}")

except ValueError as e:
    print(f"Erro: {e}")
