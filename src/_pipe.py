import pygame # biblioteca de jogos do Python
import os # integra o codigo com o com arquivos do computador
import random # gera numeros aleatórios

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'pipe.png')))



class Pipe:
# Classe que representa os canos
    DISTANCE = 250 
    SPEED = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.pos_top = 0
        self.pos_base = 0
        self.PIPE_TOP = pygame.transform.flip(IMG_PIPE, False, True)
        self.PIPE_BASE = IMG_PIPE
        self.passed = False
        self.define_height()
        
    def define_height(self):
        self.height = random.randrange(50, 450)
        self.pos_top = self.height - self.PIPE_TOP.get_height()
        self.pos_base = self.height + self.DISTANCE

    def move(self):
        self.x -= self.SPEED

    def draw(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.pos_top))
        screen.blit(self.PIPE_BASE, (self.x, self.pos_base))

    def collision(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        base_mask = pygame.mask.from_surface(self.PIPE_BASE)
        
        distance_top = (self.x - bird.x, self.pos_top - round(bird.y))
        distance_base = (self.x - bird.x, self.pos_base - round(bird.y))

        top_collision_point = bird_mask.overlap(top_mask, distance_top)
        base_collision_point = bird_mask.overlap(base_mask, distance_base)

        if top_collision_point or base_collision_point:
            return True
        else:
            return False