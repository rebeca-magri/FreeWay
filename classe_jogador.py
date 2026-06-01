import pygame

class Jogador:
    def __init__ (self): # Atributos do jogador
        #Carregando imagens
        self.imagem = pygame.image.load("src/img/tiocris.png") 
        self.imagem = pygame.transform.scale_by(self.imagem,(0.2))

        self.pos_x = 300
        self.pos_y = 200

    def andar (self,tecla_pressionada):

    #DIREITA
    if tecla_presionada [pygame.K_RIGHT]:
        if self.pos_x < 800 - self.imagem.get_width():  #700
            self.pos_x += 50 #Faz andar para direita
    
    #ESQUERDA CERTO
    if tecla_presionada [pygame.K_LEFT]:
        if self.pos_x > 0:
            self.pos_x -= 50 #Faz andar para esquerda

    #CIMA CERTO
    if tecla_presionada [pygame.K_UP]:
        if self.pos_y > 0:
            self.pos_y -= 50 #Faz andar para cima

    #BAIXO
    if tecla_presionada [pygame.K_DOWN]:
        if self.pos_y < 500 - tiocris.get_width(): 
            self.pos_y += 50 #Faz andar para baixo
