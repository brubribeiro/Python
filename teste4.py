largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while largura <= altura:
    print("#", end = "")
    coluna = 2
    while coluna < altura:
        if largura == 1 or largura == altura:
            print("#", end = "")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("#")
    largura = largura5 + 1
    
