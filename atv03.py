def tabela_verdade(P, Q, M):
    print(f'{"P":<5} {"Q":<5} {"M":<5} {"P→Q":<5} {"P∨Q":<5} {"R":<5} {"M→R":<5} {"¬P→(M→R)":<10}')
    print('-' * 50)

    P_imp_Q = not P or Q
    P_or_Q = P or Q

    if P:
        R = True
    else:
        R = Q and M

    M_imp_R = Q and M and R
    
    not_P_imp_M_imp_R = (not P and M_imp_R)

    print(f'{P:<5} {Q:<5} {M:<5} {P_imp_Q:<5} {P_or_Q:<5} {R:<5} {M_imp_R:<5} {not_P_imp_M_imp_R:<10}')

try:
    P = input("Digite o valor de P (V/F): ").strip().upper() == 'V'
    Q = input("Digite o valor de Q (V/F): ").strip().upper() == 'V'
    M = input("Digite o valor de M (V/F): ").strip().upper() == 'V'

    tabela_verdade(P, Q, M)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
