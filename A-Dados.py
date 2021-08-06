dados = int(input())
pontos = input()
pontos = pontos.split(' ')
luisa = 0
antonio = 0
pessoa = 0

for vez in pontos:
    pessoa += 1
    if pessoa == 3:
        pessoa = 1

    if pessoa == 1:
        luisa += int(vez)

    elif pessoa == 2:
        antonio += int(vez)

    if int(vez) == 6 and pessoa == 1:
        pessoa = 0
    elif int(vez) == 6 and pessoa == 2:
        pessoa = 1
    elif pessoa == 2:
        pessoa = 0

if luisa > antonio:
    print('LUISA {}'.format(luisa))
elif antonio > luisa:
    print('ANTONIO {}'.format(antonio))
else:
    print('EMPATE {}'.format(antonio))