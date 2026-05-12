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
xPare = 700
yPare = 0
larPare = 80
altPare = random.randint(20, 200)
xPare2 = 700
yPare2 = 600
larPare2 = 80
altPare2 = random.randint(400, 580)
fps = pygame.time.Clock()
os.system('cls')
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(120)
    pygame.draw.rect (tela, preto, (xPare, yPare, larPare, altPare))
    pygame.draw.rect (tela, preto, (xPare2, yPare2, larPare2, altPare2))
    pygame.display.update()
pygame.quit()
