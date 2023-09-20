import pygame  
pygame.init()

while True:
    for event in pygame.event.get():
        pass

    screen = pygame.display.set_mode()
    screen.fill("white")
    pygame.draw.circle(screen, "navyblue", [800,350], 80)
    pygame.display.flip()
    pygame.time.wait(500)
    pygame.draw.circle(screen, "blue", [800,500], 120)
    pygame.display.flip()
    pygame.time.wait(500)
    pygame.draw.circle(screen, "skyblue", [800,700], 150)
    pygame.display.flip()
    pygame.time.wait(500)

    break

