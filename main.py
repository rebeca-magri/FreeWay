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

tela = pygame.display.set_mode((800,500)) #Cria a janela do jogo, e seu tamanho tbm
pygame.display.set_caption("FREEWAY") #Nome do jogo
tela.fill(cores["AZUL CIANO"]) #Cor da tela

tiocris = pygame.image.load("src/img/tiocris.png") #Carregando imagens
tiocris = pygame.transform.scale_by(tiocris,(0.3))

posiç_tiocris_x = 0
posiç_tiocris_y = 0

while True:
    lista_eventos = pygame.event.get() #Pego todos os eventos que aconteceu na janela
    for evento in lista_eventos: #Percorro todos os eventos para encontrar aquele que eu quiser
        if evento.type == pygame.QUIT:
            pygame.quit()

    tela.fill(cores["AZUL CIANO"])

    tela.blit(tiocris,(posiç_tiocris_x,posiç_tiocris_y)) #Inserindo o tio cris na tela
    
    #DIREITA
    tecla_presionada = pygame.key.get_pressed() #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    if tecla_presionada [pygame.K_RIGHT]:
        posiç_tiocris_x += 50 #Faz andar para direita

    if tecla_presionada [pygame.K_RIGHT]: #Corrigir DPS

        posiç_tiocris_x -= 10 #Faz andar para direita

    #ESQUERDA
    tecla_presionada = pygame.key.get_pressed() #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    if tecla_presionada [pygame.K_LEFT]:
        posiç_tiocris_x -= 50 #Faz andar para esquerda

    #CIMA
    tecla_presionada = pygame.key.get_pressed() #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    if tecla_presionada [pygame.K_UP]:
        posiç_tiocris_y -= 50 #Faz andar para cima

    #BAIXO
    tecla_presionada = pygame.key.get_pressed() #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    if tecla_presionada [pygame.K_DOWN]:
        posiç_tiocris_y += 50 #Faz andar para baixo

    pygame.display.update() #Atualiza a tela

    clock.tick(8)