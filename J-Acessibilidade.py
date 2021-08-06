while True:
    alt,comp,larg=map(float, input().split(" "))
    if alt == 0.0 and comp == 0.0 and larg == 0.0:
        break
    else:
        i = (alt*100)/comp
        if i <= 8.334 and larg >= 0.8:
            print('PROJETO SIMPLES')
        else:
            print('PROJETO ESPECIAL')
