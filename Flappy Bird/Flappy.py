import pygame

preto = (0,0,0)
branco = (255,255,255)

def flappy(tela, x, y):

    pygame.draw.circle(tela,preto,(x, y),25)
    pygame.draw.polygon(tela,preto,[(x+10, y+20),(x+10, y-20),(x+35, y)])
    pygame.draw.circle(tela,branco,(x+13, y-15),6)
    