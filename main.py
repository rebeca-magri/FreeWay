import pygame
pygame.init()
from classe_inimigo import Inimigo

#lista de cores que será utilizado no jogo
cores = {                   
    "AMARELO" : (255,255,0),
    "VERDE" : (0,255,255),
    "VERMELHO" : (255,0,0),
    "AZUL CIANO" : (0,255,255)
    }

clock = pygame.time.Clock()

tela = pygame.display.set_mode((800,500)) #Cria a tela, e o tamanho da janela do jogo
pygame.display.set_caption("FREEWAY") #Título do jogo
tela.fill(cores["AZUL CIANO"]) #Cor da tela

tiocris = pygame.image.load("src/img/tiocris.png") #Carregando imagens
tiocris = pygame.transform.scale_by(tiocris,(0.2)) 
campo = pygame.image.load("src/img/campofut.webp")
campo = pygame.transform.scale(campo,(800,500))

#criando uma lista de inimigos
lista_inimigos = [Inimigo("src/img/mininoney.png"),
                  Inimigo("src/img/Messi-correndo-removebg-preview.png"),
                  Inimigo("src/img/mininoney.png"),
                  Inimigo("src/img/Messi-correndo-removebg-preview.png"),
                  Inimigo("src/img/mininoney.png"),
                  Inimigo("src/img/Messi-correndo-removebg-preview.png"),]


posiç_tiocris_x = 300
posiç_tiocris_y = 200

while True: 
    lista_eventos = pygame.event.get() #Pego todos os eventos que aconteceu na janela
    for evento in lista_eventos: #Percorro todos os eventos para encontrar aquele que eu quiser
        if evento.type == pygame.QUIT: # X para fechar o programa
            pygame.quit()
            exit()

    tela.fill(cores["AZUL CIANO"])
    tela.blit(campo,(0,0)) #Inserindo o campo na tela

    tela.blit(tiocris,(posiç_tiocris_x,posiç_tiocris_y)) #Inserindo o tio cris na tela

    #Inserindo inimigos na tela
    for inimigo in lista_inimigos:
        inimigo.andar()
        inimigo.exibir(tela)


    ###TIO CRIS###
    #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    tecla_presionada = pygame.key.get_pressed() #Inserir apenas uma vez, se não dá erro!

    #DIREITA
    if tecla_presionada [pygame.K_RIGHT]:
        if posiç_tiocris_x < 800 - tiocris.get_width():  #700
            posiç_tiocris_x += 50 #Faz andar para direita
    
    #ESQUERDA CERTO
    if tecla_presionada [pygame.K_LEFT]:
        if posiç_tiocris_x > 0:
            posiç_tiocris_x -= 50 #Faz andar para esquerda

    #CIMA CERTO
    if tecla_presionada [pygame.K_UP]:
        if posiç_tiocris_y > 0:
            posiç_tiocris_y -= 50 #Faz andar para cima

    #BAIXO
    if tecla_presionada [pygame.K_DOWN]:
        if posiç_tiocris_y < 500 - tiocris.get_width(): 
            posiç_tiocris_y += 50 #Faz andar para baixo


    pygame.display.update() #Atualiza a tela
    clock.tick(60)