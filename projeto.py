#1. Faça um programa que leia uma senha e:
#   * informe que a senha é fraca caso tenha menos de 5 caracteres;
#   * continue solicitando um novo valor para senha enquanto a senha for fraca.
print('-=-'*20)
senhas = ''
while len(senhas) < 5:
    senhas = input('digite sua senha: ')
    if len(senhas) <5:
        print('Sua senha é fraca, digite outra senha')
    else:
        print(f'Sua senha contem é forte e {len(senhas)} caracteres')
print('-=-'*20)