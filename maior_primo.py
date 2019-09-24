def maior_primo(n):
    aux = n
    while aux > 2:
        if éprimo(aux):
            return aux
        aux -= 1
    return 2
def éprimo(k):
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True
    
