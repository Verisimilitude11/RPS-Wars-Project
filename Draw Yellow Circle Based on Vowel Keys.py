import random
import pygame
pygame.init()

def draw_circle(window, color=(255, 255, 255)):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    size = random.randint(20, 30)
    pygame.draw.circle(window, color, (x, y), size)

w = pygame.display.set_mode([500, 500])
w.fill((0, 0, 0))

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                draw_circle(w, (255, 255, 0))
            elif event.key == pygame.K_e:
                draw_circle(w, (255, 255, 0))
            elif event.key == pygame.K_i:
                draw_circle(w, (255, 255, 0))
            elif event.key == pygame.K_o:
                draw_circle(w, (255, 255, 0))
            elif event.key == pygame.K_u:
                draw_circle(w, (255, 255, 0))
            else:
                draw_circle(w, (255, 255, 255))

    pygame.display.flip()
