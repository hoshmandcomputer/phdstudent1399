import pygame, sys

pygame.init(); clock = pygame.time.Clock()
scr = pygame.display.set_mode((640, 480))

image = pygame.image.load('ufo.png')
rect = image.get_rect()
rect.center = (320, 240)

while True:
    pygame.display.flip()
    clock.tick(60)
    scr.fill((0, 0, 0))
    scr.blit(image, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    if pygame.mouse.get_pressed()[0]:
        if rect.collidepoint(pygame.mouse.get_pos()):
            print ('The mouse was click inside the image.')