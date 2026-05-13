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
gravidade = 0.2
xPare = 1500
yPare = 0
larPare = 80
altPare = random.randint(20, 400)
yPare2 = altPare + 180
larPare2 = 80
altPare2 = 600
xPare3 = 1000
fps = pygame.time.Clock()
os.system('cls')
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE or evento.key == pygame.K_UP:
                pulo = -6.5

    tela.fill(branco)
    fps.tick(120)
    pulo += gravidade
    y += pulo
    pygame.draw.circle(tela,amarelo,(x, y),25)
    pygame.draw.polygon(tela,vermelho,[(x+10, y+22),(x+20, y-13),(x+35, y+5)])
    pygame.draw.circle(tela,branco,(x+13, y-15),6)
    pygame.draw.circle(tela,preto,(x+13, y-15),3)
    pygame.draw.rect (tela, preto, (xPare, yPare, larPare, altPare))
    pygame.draw.rect (tela, preto, (xPare, yPare2, larPare2, altPare2))
    passaro = pygame.Rect(x-25, y-25, 50, 50)
    paredeCima = pygame.Rect(xPare, yPare, larPare, altPare)
    paredeBaixo = pygame.Rect(xPare, yPare2, larPare2, altPare2)
    xPare -= 3
    xPare3 -= 3
    if xPare <= -80:
        xPare = 810
        altPare = random.randint(20, 400)
        yPare2 = altPare + random.randint(125,300)
    if y > 620 or y < -20 or passaro.colliderect(paredeCima) or passaro.colliderect(paredeBaixo):
        rodando = False

    pygame.display.update()
pygame.quit()
 