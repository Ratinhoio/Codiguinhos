import pygame
import time
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
rodando = True
ino = True
subino = True 
xBola = 400
yBola = 300
velo = 1
fps = pygame.time.Clock()
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(120)
    pygame.draw.circle( tela, preto, (xBola, yBola), 50) # largura, altura e raio
    if xBola <= 50:
        ino = True
        velo += 1
    elif xBola >= 750:
        ino = False
        velo += 1
    if ino:
        xBola += velo
    else:
        xBola -= velo
        
    if yBola <= 50:
        subino = True
        velo += 1
    elif yBola >= 550:
        subino = False
        velo += 1
    if subino:
        yBola += velo
    else:
        yBola -= velo
        
    pygame.display.update()
pygame.quit()