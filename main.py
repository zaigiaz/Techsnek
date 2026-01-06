import pygame

# create basic game loop that displays grid
 
# game loop:
# init(), processinput(), update(), render(), and run()

pygame.init()
window = pygame.display.set_mode((1920,1080))
pygame.key.set_repeat(500, 30)
font = pygame.font.Font(None, 74)
text = font.render("Hello, Pygame!", True, (0, 255, 0))

x = 200
y = 200
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
                break
            elif event.key == pygame.K_RIGHT:
                x += 50
            elif event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_DOWN:
                y += 50
            elif event.key == pygame.K_UP:
                y -= 50

    window.fill((0,0,0))
    window.blit(text, (250, 250))
    pygame.draw.rect(window,(0,0,255),(x,y,240,240))
    pygame.display.update()

pygame.quit()








