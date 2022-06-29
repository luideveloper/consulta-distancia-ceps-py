from functions import distanceInfoCeps

print("\x1b[2J\x1b[1;1H")
print("Digite a abaixo os CEPs que você desejar saber a distância: \n")
cep1 = input('> Primeiro cep: ')
cep2 = input('> Segundo cep: ')

if len(cep1) and len(cep2) != 8:
    print("\x1b[2J\x1b[1;1H")
    print("Quantidade de dígitos inválida")
    exit()
else:
    distanceInfoCeps(cep1, cep2)


