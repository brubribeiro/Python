def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [1,2,1,3,2,4,3,5]

lista = remove_repetidos(lista)
print (lista)
