from random import randint
lista2 = list()
contador2 = 0
retorno = list()
for cont in range(0, 10):
    while True:
        numero = randint(0, 25)
        if numero not in lista2:
            lista2.append(numero)
            contador2 += 1
        if contador2 == 15:
            break
    contador2 = 0
    retorno.append(sorted(lista2.copy()))
    lista2.clear()
print(retorno)