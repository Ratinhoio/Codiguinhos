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
xBola = 0
yBola = 300
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
    elif xBola >= 750:
        ino = False
    if ino:
        xBola += 1
    else:
        xBola -= 1
        
    if yBola <= 50:
        subino = True
    elif yBola >= 550:
        subino = False
    if subino:
        yBola += 1
    else:
        yBola -= 1
        
        
    pygame.display.update()
pygame.quit()