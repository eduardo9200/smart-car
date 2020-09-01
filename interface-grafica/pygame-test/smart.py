import pygame
import PySimpleGUI as sg
import webbrowser

pygame.init()

size = width, height = 800, 600

tela = pygame.display.set_mode(size)
pygame.display.set_caption("Smart Car")
imagem_fundo = pygame.image.load('img.png')

janela_aberta = True

while janela_aberta:

    pygame.time.delay(50) #milissegundos

    for event in pygame.event.get():
        #Clicou no botão Fechar
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos_clique_unico = pygame.key.get_pressed()

        #Tira print
        if comandos_clique_unico[pygame.K_p]:
            print("Clicou em p")

        #Grava vídeo (play/pause)
        if comandos_clique_unico[pygame.K_r]:
            print("Clicou em r")

        #Ativa/desativa visão computacional
        if comandos_clique_unico[pygame.K_v]:
            print("Clicou em v")
        
        if comandos_clique_unico[pygame.K_c]:
            print("Clicou em c")
            #Captura o IP da Jetson no momento da inicialização
            ip = sg.PopupGetText('Informe o IP da Jetson para acessar sua câmera', 'IP Jetson')
            
            if not(ip is None) and (ip != ""):
                #Abre o navegador com o IP informado, desde que ele seja diferente de None/Null e não esteja vazio
                webbrowser.open('http://{}:8000'.format(ip), new=0, autoraise=True)
        
        #Fecha a janela
        if comandos_clique_unico[pygame.K_ESCAPE]:
            janela_aberta = False
            print("Clicou em ESC")


    #Lê a tecla pressionada pelo usuário e executa a ação enquanto a tecla estiver pressionada
    comandos = pygame.key.get_pressed()

    #Camera para cima
    if comandos[pygame.K_UP]:
        print("clicou seta para cima")
        
    #Camera para baixo
    if comandos[pygame.K_DOWN]:
        print("clicou seta para baixo")
        
    #Carro para frente
    if comandos[pygame.K_w]:
        print("clicou w (frente)")
    
    #Carro para trás
    if comandos[pygame.K_s]:
        print("clicou s (trás)")

    #Carro para esquerda
    if comandos[pygame.K_a]:
        print("clicou a (esquerda)")
        
    #Carro para direita
    if comandos[pygame.K_d]:
        print("clicou d (direita)")
    
    #pygame.draw.circle(tela, (0,255,0), (400,300), 50)
    tela.blit(imagem_fundo,(0,0)) #Carrega imagem da variável imagem_fundo na tela
    pygame.display.update()

pygame.quit()