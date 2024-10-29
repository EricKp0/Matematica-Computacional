def triangulos_semelhantes():
    print("Os triângulos são semelhantes!")

def triangulos_nao_semelhantes():
    print("Os triângulos não são semelhantes!")

def criterioLAL(a, b, c, d, f, g):
    if a / b == c / d and f == g:
        triangulos_semelhantes()
    else:
        triangulos_nao_semelhantes()

def criterioAA(ang1, ang2, ang3, ang4):
    if ang1 == ang3 and ang2 == ang4:
        triangulos_semelhantes()
    elif ang1 == ang4 and ang2 == ang3:
        triangulos_semelhantes()
    else:
        triangulos_nao_semelhantes()

def criterioLLL(a, b, c, d, e, f):
    if a / d == b / e == c / f:
        triangulos_semelhantes()
    else:
        triangulos_nao_semelhantes()

while True:

    print("Usar zero em ângulos não conhecidos");

    lado11 = float(input("Lado 1 do triângulo 1: "))
    lado12 = float(input("Lado 2 do triângulo 1: "))
    lado13 = float(input("Lado 3 do triângulo 1: "))
    angulo11 = float(input("Ângulo 1 do triângulo 1: "))
    angulo12 = float(input("Ângulo 2 do triângulo 1: "))
    angulo13 = float(input("Ângulo 3 do triângulo 1: "))

    if (angulo11 + angulo12 + angulo13) > 180:
        print("Erro, a soma dos ângulos do triângulo 1 é maior que 180°")
        break

    lado21 = float(input("Lado 1 do triângulo 2: "))
    lado22 = float(input("Lado 2 do triângulo 2: "))
    lado23 = float(input("Lado 3 do triângulo 2: "))
    angulo21 = float(input("Ângulo 1 do triângulo 2: "))
    angulo22 = float(input("Ângulo 2 do triângulo 2: "))
    angulo23 = float(input("Ângulo 3 do triângulo 2: "))

    if (angulo21 + angulo22 + angulo23) > 180:
        print("Erro, a soma dos ângulos do triângulo 2 é maior que 180°")
        break

    def main():
        print("1 - Verificar com LAL")
        print("2 - Verificar com AA")
        print("3 - Verificar com LLL")
        opcao = int(input("Insira sua opção: "))

        if opcao == 1:
            criterioLAL(lado11, lado21, lado12, lado22, angulo12, angulo22)
        elif opcao == 2:
            criterioAA(angulo11, angulo12, angulo21, angulo22)
        elif opcao == 3:
            criterioLLL(lado11, lado12, lado13, lado21, lado22, lado23)
        else:
            print("Opção inválida.")

    main()
