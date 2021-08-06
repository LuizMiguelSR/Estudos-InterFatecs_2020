comprimento = int(input('Comprimento: '))
largura = 0
comprInicio = comprimento
dna = input('DNA: ')
comp = []
ultimo = len(dna) - comprInicio
igual = 0

for x in dna:
    comp += x

while largura <= ultimo:
    compara1 = comp[largura:comprimento]
    compara2 = compara1[::-1]
    if compara1 == compara2:
        igual = 1
    comprimento += 1
    largura += 1
if igual == 1:
    print('S')
else:
    print('N')
