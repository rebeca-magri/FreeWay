import pygame

class Jogador:
    def __init__ (self): # Atributos do jogador
        #Carregando imagens
        self.imagem = pygame.image.load("src/img/tiocris.png") 
        self.imagem = pygame.transform.scale_by(self.imagem,(0.1))

        self.pos_x = 300
        self.pos_y = 0

        #máscara para verificar a colisão
        self.mascara = pygame.mask.from_surface(self.imagem)
        self.vidas = 0

    def andar (self,teclas_pressionadas):

        #DIREITA
        if teclas_pressionadas [pygame.K_RIGHT]:
            if self.pos_x < 800 - self.imagem.get_width():  
                self.pos_x += 20 #Faz andar para direita
        
        #ESQUERDA CERTO
        if teclas_pressionadas [pygame.K_LEFT]:
            if self.pos_x > 0:
                self.pos_x -= 20 #Faz andar para esquerda

        #CIMA CERTO
        if teclas_pressionadas [pygame.K_UP]:
            if self.pos_y > 0:
                self.pos_y -= 20 #Faz andar para cima

        #BAIXO
        if teclas_pressionadas [pygame.K_DOWN]:
            if self.pos_y < 500 - self.imagem.get_width(): 
                self.pos_y += 20 #Faz andar para baixo

        if self.pos_y >= 500 - self.imagem.get_height():
            self.vidas += 1
            self.voltar()
            pygame.time.delay(800)

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem, (self.pos_x, self.pos_y))

    def voltar(self):
        self.pos_x = 300
        self.pos_y = 0

        pygame.init()
        pygame.mixer.init()

        # Carrega e toca o arquivo
        pygame.mixer.music.load('src/sound/suuuurcr7.mp3')
        pygame.mixer.music.play()