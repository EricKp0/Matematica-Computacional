def calcular_salario(salario_fixo, comissao_por_carro, total_vendas, numero_carros_vendidos):
    salario_final = salario_fixo
    
    if numero_carros_vendidos > 0:
        salario_final += comissao_por_carro * numero_carros_vendidos  
        salario_final += 0.05 * total_vendas  
        
        if numero_carros_vendidos > 10:
            salario_final += 0.10 * total_vendas  

    return salario_final

salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
comissao_por_carro = float(input("Digite a comissão fixa por carro vendido: R$ "))
total_vendas = float(input("Digite o total de vendas realizadas: R$ "))
numero_carros_vendidos = int(input("Digite o número de carros vendidos: "))

salario_vendedor = calcular_salario(salario_fixo, comissao_por_carro, total_vendas, numero_carros_vendidos)

print(f"O salário final do vendedor é: R$ {salario_vendedor:.2f}")
