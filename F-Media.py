import statistics
cont = soma = media =  0
lista=list()
while True:
    qtdea=input().upper().strip()
    if qtdea in 'EOF':
        break
    else:
        qtdea2=int(qtdea)
        for c in range(0,qtdea2):
            idade=int(input())
            lista.append(idade)
        moda = statistics.multimode(lista)            
        print('MODA={}'.format(moda))
        media=statistics.mean(lista)
        print('MEDIA={:.2f}'.format(media))
        mediana = statistics.median(lista)
        print('MEDIANA={:.2f}'.format(mediana))
        lista.clear()
