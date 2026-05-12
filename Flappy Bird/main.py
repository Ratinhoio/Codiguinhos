import pygame, time, os
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
fps = pygame.time.Clock()
os.system('cls')
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(120)
    pulo += gravidade
    y += pulo
    flappy(tela, x, y)
    pygame.key.get_pressed()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        pulo = -10
        
    pygame.display.update()
pygame.quit()
