import pygame, time, random, os
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
rodando = True
xBola = 400
yBola = 300
rBola = 15
xBola2 = random.randint (50, 750)
yBola2 = random.randint (50, 550)
fps = pygame.time.Clock()
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(60)
    bola = pygame.Rect(xBola - rBola, yBola - rBola, rBola * 2, rBola * 2)
    bola2 = pygame.Rect(xBola2 - 10, yBola2 - 10, 20, 20)

    if bola.colliderect(bola2):
        xBola2 = random.randint(50, 750)
        yBola2 = random.randint(50, 550)
        rBola += 5
    pygame.draw.circle( tela, vermelho, (xBola2, yBola2), 10)
    pygame.draw.circle( tela, preto, (xBola, yBola), rBola)
    pygame.key.get_pressed()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_d]:
        xBola += 15
    if teclas[pygame.K_a]:
        xBola -= 15
    if teclas[pygame.K_s]:
        yBola += 15
    if teclas[pygame.K_w]:
        yBola -= 15
    if xBola >= 800:
        xBola = 0
    elif xBola <= 0:
        xBola = 800
    elif yBola >= 600:
        yBola = 0
    elif yBola <= 0:
        yBola = 600
    pygame.display.update()
pygame.quit()