import pygame
pygame.init()

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
tiocris = pygame.transform.scale_by(tiocris,(0.3)) 
campo = pygame.image.load("src/img/campofut.webp")
campo = pygame.transform.scale(campo,(800,500))
messi = pygame.image.load("src/img/Messi-correndo-removebg-preview.png")
messi = pygame.transform.scale_by(messi,(0.3)) 

posiç_tiocris_x = 300
posiç_tiocris_y = 200
posiç_messi_x = 400
posiç_messi_y = 200
velocidade_messi_x = 90

while True: 
    lista_eventos = pygame.event.get() #Pego todos os eventos que aconteceu na janela
    for evento in lista_eventos: #Percorro todos os eventos para encontrar aquele que eu quiser
        if evento.type == pygame.QUIT: # X para fechar o programa
            pygame.quit()
            exit()

    tela.fill(cores["AZUL CIANO"])
    tela.blit(campo,(0,0)) #Inserindo o campo na tela
    tela.blit(messi,(posiç_messi_x,posiç_messi_y)) #Inserindo o rival messi na tela
    tela.blit(tiocris,(posiç_tiocris_x,posiç_tiocris_y)) #Inserindo o tio cris na tela
    
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
    
    ###MESSI###
    #Fazer o messi andar sozinho left para right e vice versa
    if 1 == 1:
        posiç_messi_x += velocidade_messi_x
        if posiç_messi_x >= 800 - messi.get_height() or posiç_messi_x <= 0:
            velocidade_messi_x = -velocidade_messi_x #Ele muda o lado

    pygame.display.update() #Atualiza a tela

    clock.tick(8)