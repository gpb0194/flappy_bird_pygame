import pygame # biblioteca de jogos do Python
import os # integra o codigo com o com arquivos do computador

IMGS_BIRD = [
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_up.png'))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_flat.png'))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_down.png')))
            ]
           


class Bird:
# Classe que representa o pássaro do jogo
    IMGS = IMGS_BIRD
    # animações da rotação 
    ROTATION_MAX = 25
    ROTATION_SPEED = 20
    ANIMATION_TIME = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.time = 0
        self.count_imgs = 0
        self.image = self.IMGS [0]

    def jump(self):
        self.speed = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        # calcular o deslocamento
        self.time += 1
        motion = 1.5 * (self.time ** 2) + self.speed * self.time
        
        # restringir o deslocamento
        if motion > 16:
            motion = 16
        elif motion < 0:
            motion -= 2

        self.y += motion

        # o ângulo do pássaro
        if motion < 0 or self.y < (self.height + 50):
            if self.angle < self.ROTATION_MAX:
                self.angle = self.ROTATION_MAX
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

    def draw(self, screen):
        # definir qual imagem do passaro vai usar
        self.count_imgs += 1
        
        if self.count_imgs < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.count_imgs < self.ANIMATION_TIME * 2:
            self.image = self.IMGS[1]
        elif self.count_imgs < self.ANIMATION_TIME * 3:
            self.image = self.IMGS[2]    
        elif self.count_imgs < self.ANIMATION_TIME * 4:
            self.image = self.IMGS[1]
        elif self.count_imgs >= self.ANIMATION_TIME * 4 + 1:
            self.image = self.IMGS[0]
            self.count_imgs = 0
        
        # se o passaro tiver caindo não vai bater asas
        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.count_imgs = self.ANIMATION_TIME * 2

        # desenhar a imagem
        img_rotate = pygame.transform.rotate(self.image, self.angle)
        pos_center_img = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = img_rotate.get_rect(center=pos_center_img)
        screen.blit(img_rotate, rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
