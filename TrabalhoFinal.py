import random

def menu(nome,l):
    print("-----------Menu-----------")
    print("Olá %s"%nome)
    b=int(input("\nEscolha o numero da sua ação\n1-Para jogar(Pedra,papel e Tesoura)\n2-Para digitar um novo nome(apaga e altera o anterior)\n3-Mostrar quantidades de empates,vitorias e derrotas\nQual sua opção:"))
    if b==1:
        a = 1

        while a > 0 and a < 4:
            a = int(input("Digite o numero que representa sua escolha!! \nSendo Pedra=1,Papel=2,Tesoura=3 e difentes desses retorna ao menu:"))
            print("-------->Dado armazenado<----------")
            jogos(a,l)
    if b==2:
        del l
        l=[]
        nome=input("Digite seu nome:")
        menu(nome,l)
    if b==3:
        print(l)
        menu(nome,l)
def jogos(a,l):
    ppt = ['pedra', 'papel', 'tesoura']
    x = random.choice(ppt)
    if a==1:
        if x == 'pedra':
            l.append('Empatou')
        elif x == 'papel':
            l.append('Perdeu')
        elif x == 'tesoura':
            l.append('Ganhou')

    elif a == 2:
        if x == 'pedra':
            l.append('Ganhou')
        elif x == 'papel':
            l.append('Empatou')
        elif x == 'tesoura':
            l.append('Perdeu')

    elif a == 3:
        if x == 'pedra':
            l.append('Perdeu')
        elif x == 'papel':
            l.append('Ganhou')
        elif x == 'tesoura':
            l.append('Empatou')

    else:
        menu(nome,l)
nome=input("Antes de começar digite seu nome e logo em seguida sera levado para o menu:")
l=[]
menu(nome,l)
