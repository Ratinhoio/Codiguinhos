import pygame, os, time, random

pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")
branco = (255,255,255)
preto = (0,0,0)
verde = (0,255,0)
vermelho = (255,0,0)
cinza = (128,128,128)
fps = pygame.time.Clock()
rodando = True
xCobra = 100
yCobra = 100
while rodando:
    fps.tick(8)
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    for linhaVertical in range(0, 800, 50):
        pygame.draw.line(tela, cinza, (linhaVertical, 100), (linhaVertical, 600))
    for linhaHorizontal in range(100, 600, 50):
        pygame.draw.line(tela, cinza, (0, linhaHorizontal), (900, linhaHorizontal))
    pygame.draw.rect(tela, verde, (xCobra, yCobra, 50, 50))
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        xCobra -= 50
        time.sleep(0.5)
    if teclas[pygame.K_RIGHT]:
        xCobra += 50
        time.sleep(0.5)
    pygame.display.update()
    
pygame.quit()