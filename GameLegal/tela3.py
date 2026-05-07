import pygame
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
rodando = True
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    pygame.draw.line( tela, preto, (50,20), (750, 20))
    pygame.draw.line( tela, preto, (50,20), (400, 550))
    pygame.draw.line( tela, preto, (750,20), (400, 550))
    pygame.display.update()
pygame.quit()