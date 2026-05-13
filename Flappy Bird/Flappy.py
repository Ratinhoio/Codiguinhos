import pygame

preto = (0,0,0)
branco = (255,255,255)
amarelo = (236,208,22)
vermelho = (240,0,0)

def flappy(tela, x, y):

    pygame.draw.circle(tela,amarelo,(x, y),25)
    pygame.draw.polygon(tela,vermelho,[(x+10, y+22),(x+20, y-13),(x+35, y+5)])
    pygame.draw.circle(tela,branco,(x+13, y-15),6)
    pygame.draw.circle(tela,preto,(x+13, y-15),3)
    