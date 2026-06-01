import pygame
import random

class Inimigo: 

    def __init__(self, endereco_imagem):  # Atributos do rival, Messi
        # Carregando imagens
        self.imagem = pygame.image.load(endereco_imagem)  
        self.imagem = pygame.transform.scale_by(self.imagem, 0.3)

        # Definindo posições e a velocidade
        self.x = 400  
        self.y = random.randint(20, 400)
        self.velocidade_x = random.randint(5,30)
        
    def andar(self):
        # O Messi anda sempre para a frente
        self.x += self.velocidade_x
        
        if self.x > 800:
            self.voltar()

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem, (self.x, self.y))

    def voltar(self):
        self.x = 0
        self.y = random.randint(20, 300)
        self.velocidade_x = random.randint(10,30)
