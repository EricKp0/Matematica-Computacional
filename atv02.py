def razao_bissetriz(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a / b
    else:
        return "Os lados informados não formam um triângulo."

def divisao_bissetriz_externa(a, b, c):

    if b == c:
        return "Os lados b e c precisam ser diferentes."

    razao = (b + c) / abs(b - c)
    d = a * razao / (1 + razao)
    e = a - d
    
    return d, e

def main():
    print("> MENU <")
    print("1 - Parte A (Bissetriz Interna)")
    print("2 - Parte B (Bissetriz Externa)")
    
    opcao = int(input("Digite o número da opção: "))
    
    if opcao == 1:
        a = float(input("Digite o comprimento do lado a: "))
        b = float(input("Digite o comprimento do lado b: "))
        c = float(input("Digite o comprimento do lado c: "))
        
        resultado = razao_bissetriz(a, b, c)
        print(f"A razão das partes formadas pela bissetriz interna é: {resultado:.2f}" if isinstance(resultado, float) else resultado)
    
    elif opcao == 2:
        a = float(input("Digite o valor do lado a: "))
        b = float(input("Digite o valor do lado b: "))
        c = float(input("Digite o valor do lado c: "))
        
        resultado = divisao_bissetriz_externa(a, b, c)
        if isinstance(resultado, tuple):
            d, e = resultado
            print(f"Os segmentos formados pela bissetriz externa no lado oposto são: d = {d:.2f} e e = {e:.2f}")
        else:
            print(resultado)
    
    else:
        print("Essa escolha não existe")

main()
