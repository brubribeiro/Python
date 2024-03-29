def partida():    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))   
    x = n % (m + 1)   
    primeira_vez_usuario = False
    primeira_vez_computador = False

    if x != 0: 
        pcJoga = True
        primeira_vez_computador = True 
    if x == 0: 
        pcJoga = False
        primeira_vez_usuario = True     
    while n > 0:
        if pcJoga == True: 
            if primeira_vez_computador == True:
                print("")
                print("Computador começa!")
                print("")
            primeira_vez_computador = False            
            vlr_tirado = computador_escolhe_jogada(n,m)           
            pcJoga = False            
            if vlr_tirado == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou ",vlr_tirado," peças.")
        else:            
            if primeira_vez_usuario == True:
                print("")
                print("Voce começa!")
                print("")
            primeira_vez_usuario = False 
            vlr_tirado = usuario_escolhe_jogada(n,m)            
            pcJoga = True            
            if vlr_tirado == 1:
                print("Você tirou uma peça")
            else:
                print("Voce tirou",vlr_tirado,"peças.")
        n = n - vlr_tirado
        if n > 0:
            print("Agora restam",n,"peças no tabuleiro.")
            print("")
    
    if pcJoga == True:
        print("Fim do jogo! Você ganhou!")
        print("")
        return 1 
    else:
        print("Fim do jogo! O computador ganhou!")
        print("")
        return 0 
def usuario_escolhe_jogada(n,m):
    vlr_tirado = 0    
    while vlr_tirado == 0:
        vlr_tirado = int(input("Quantas peças você vai tirar?"))       
        if vlr_tirado > n or vlr_tirado > m or vlr_tirado < 1 :
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            print("")
            vlr_tirado = 0
    return vlr_tirado

def computador_escolhe_jogada(n,m):
    if n <= m: 
        return n 
    else:
        sobrou = n % (m+1)
        if sobrou > 0:
            return sobrou
        return m

def campeonato():    
    computador = 0
    usuario = 0    
    i = 1
    for _ in range(3):
        print("**** Rodada",i,"****")
        print("")
        id_ganhou = partida()
        i = i + 1 
        if id_ganhou == 1:
            usuario = usuario +1 
        else:
            computador = computador + 1
    print("**** Final do campeonato! ****")
    print("Placar: Você",usuario,"X",computador,"Computador")

escolha = 0
while escolha == 0:
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    escolha = int(input())
    if escolha == 1:
        partida()
        break
    elif escolha == 2:
        print("Voce escolheu um campeonato!")
        print("")
        campeonato() 
        break
    else:
        print("Escolha uma opção válida!")
        print("")
        escolha = 0 
