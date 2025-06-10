import pygame #### type: ignore # biblioteca de jogos do Python
import os # integra o codigo com o com arquivos do computador
import random # gera numeros aleatórios  
from _bird import Bird
from _floor import Floor
from _pipe import Pipe

IMG_BACKGROUND =  pygame.transform.scale2x(pygame.image.load(os.path.join('assets/images', 'bg.png')))

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
          
pygame.font.init()
FONT_SCORE = pygame.font.SysFont('arial', 50)


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

main()