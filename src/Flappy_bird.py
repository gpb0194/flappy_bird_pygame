import pygame #### type: ignore # biblioteca de jogos do Python
import os # integra o codigo com o com arquivos do computador
import random # gera numeros aleatórios

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

IMG_PIPE = pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'pipe.png')))
IMG_FLOOR =  pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'floor.png')))
IMG_BACKGROUND =  pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bg.png')))
IMGS_BIRD = [
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_up.png'))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_flat.png'))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bird_down.png')))
            ]
            
pygame.font.init()
FONT_SCORE = pygame.font.SysFont('arial', 50)


class Bird:
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
        self.heght = self.y
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
        if motion < 0 or self.y < (self.heght  + 50):
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
        
        # se o passaro tiver caindo não vai bater asas
        if self.angle <= 80:
            self.image = self.IMGS[1]
            self.count_imgs = self.ANIMATION_TIME * 2

        # desenhar a imagem
        img_rotate = pygame.transform.rotate(self.image, self.angle)
        pos_center_img = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = img_rotate.get_rect(center=pos_center_img)
        screen.blit(img_rotate, rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)


class Pipe:
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


class Floor:
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


def draw_screen(screen, birds, pipes, floor, points):
    screen.blit(IMG_BACKGROUND, (0, 0))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Pontuação: {points}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))
    floor.draw(screen)
    pygame.display.update()


def main():
    birds = [Bird(230, 350)]
    floor = Floor(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    points = 0
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)
        # interação com o usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for bird in birds:
                        bird .jump()
        # mover as coisas
        for bird in birds:
            bird.move()
        floor.move()
        
        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collision(bird):
                    birds.pop(i)
                    run = False 

                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True
            pipe.move()
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)
   
        if add_pipe:
            points += 1
            pipes.append(Pipe(600))
        
        for pipe in remove_pipes:
            pipes.remove(pipe)

        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > floor.y or bird.y < 0:
                birds.pop(i)

        draw_screen(screen, birds, pipes, floor,points)

main ()