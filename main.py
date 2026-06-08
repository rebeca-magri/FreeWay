import pygame
pygame.init()
from classe_inimigo import Inimigo
from classe_jogador import Jogador

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

campo = pygame.image.load("src/img/campofut.webp")
campo = pygame.transform.scale(campo,(800,500))
fundo = pygame.image.load("src/img/iniciar.png")
fundo = pygame.transform.scale(fundo,(800,500))
perdeu = pygame.image.load("src/img/game_over.png")
perdeu = pygame.transform.scale(perdeu,(800,500))
venceu = pygame.image.load("src/img/venceuuutche.png")
venceu = pygame.transform.scale(venceu,(800,500))

#criando uma lista de inimigos
lista_inimigos = [Inimigo("src/img/mininoney.png"),
                  Inimigo("src/img/Messi-correndo-removebg-preview.png"),
                  Inimigo("src/img/mininoney.png")]

#criando o jogador
cr7 = Jogador()

status_jogo = "INICIO"

while True:

    lista_eventos = pygame.event.get() #Pego todos os eventos que aconteceu na janela
    for evento in lista_eventos: #Percorro todos os eventos para encontrar aquele que eu quiser
        if evento.type == pygame.QUIT: # X para fechar o programa
            pygame.quit()
            exit()

    #Verifica o pressionamento da tecla / Fazendo ela andar só quando pressionado
    teclas_pressionadas = pygame.key.get_pressed() #Inserir apenas uma vez, se não dá erro!

    if status_jogo == "INICIO":
        #Inserindo o fundo inicial na tela
        tela.blit(fundo,(0,0))
        if teclas_pressionadas[pygame.K_RETURN] or teclas_pressionadas[pygame.K_KP_ENTER]:
            status_jogo = "JOGANDO"

    if status_jogo == "JOGANDO":
        #Inserindo o campo na tela
        tela.blit(campo,(0,0)) 

        #Inserindo o jogador na tela
        cr7.andar(teclas_pressionadas)
        cr7.exibir(tela)
        
        fonte = pygame.font.SysFont("Calibri", 40, True, False)
        texto = fonte.render(f"Vidas = " + ('<3' * cr7.vidas), True, (255,0,0), (255,255,255))
        tela.blit(texto, (0,0))
        if cr7.vidas == 3:
            status_jogo = "VENCEU"

        #Inserindo inimigos na tela
        for inimigo in lista_inimigos:
            inimigo.andar()
            inimigo.exibir(tela)
            
            #testando se o inimigo colidiu com a vaca
            if cr7.mascara.overlap(inimigo.mascara,(inimigo.x-cr7.pos_x,inimigo.y-cr7.pos_y)):
                inimigo.voltar()
                cr7.voltar()
                status_jogo = "PERDEU"

    if status_jogo == "PERDEU":
        tela.blit(perdeu,(0,0))
        if teclas_pressionadas[pygame.K_RETURN] or teclas_pressionadas[pygame.K_KP_ENTER]:
            cr7.voltar()
            status_jogo = "INICIO"
            cr7.vidas = 0

    if status_jogo == "VENCEU":
        tela.blit(venceu,(0,0))
        if teclas_pressionadas[pygame.K_RETURN] or teclas_pressionadas[pygame.K_KP_ENTER]:
            cr7.voltar()
            status_jogo = "INICIO"
            cr7.vidas = 0

    pygame.display.update() #Atualiza a tela
    clock.tick(60)