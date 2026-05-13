import pygame, time, os, random
from Flappy import *
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
rodando = True
x = 400
y = 300
pulo = 0
gravidade = 0.3
xPare = 700
yPare = 0
larPare = 80
altPare = random.randint(100, 400)
yPare2 = altPare + 180
larPare2 = 80
altPare2 = 600
xPare3 = 1000
altPare3 = random.randint(100, 400)
yPare3 = altPare3 + 180
fps = pygame.time.Clock()
os.system('cls')
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                pulo = -8

    tela.fill(branco)
    fps.tick(120)
    pulo += gravidade
    y += pulo
    flappy(tela, x, y)
    pygame.draw.rect (tela, preto, (xPare, yPare, larPare, altPare))
    pygame.draw.rect (tela, preto, (xPare, yPare2, larPare2, altPare2))
    pygame.draw.rect (tela, preto, (xPare3, yPare, larPare, altPare3))
    pygame.draw.rect (tela, preto, (xPare3, yPare3, larPare2, altura - yPare3))
    xPare -= 3
    xPare3 -= 3
    if xPare <= -80:
        xPare = 810
        altPare = random.randint(150, 250)
        yPare2 = altPare + 180
    
    if xPare3 <= -80:
        xPare3 = 810
        altPare3 = random.randint(350, 450)
        yPare3 = altPare3 + 180
    pygame.display.update()
pygame.quit()
 