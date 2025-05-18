import pygame # biblioteca de jogos do Python
import os # integra o codigo com o com arquivos do computador

IMG_FLOOR =  pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'floor.png')))



class Floor:
    # Classe que representa o chão do jogo
    SPEED = 5
    WIDTH = IMG_FLOOR.get_width()
    IMG = IMG_FLOOR

    def __init__(self, y):
        self.y = y
        self.x0 = 0
        self.x1 = self.WIDTH

    def move(self):
        self.x0 -= self.SPEED
        self.x1 -= self.SPEED

        if self.x0 + self.WIDTH < 0:
            self.x0 = self.x1 + self.WIDTH
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x0 + self.WIDTH

    def draw(self, screen):
        screen.blit(self.IMG, (self.x0, self.y))
        screen.blit(self.IMG, (self.x1, self.y))