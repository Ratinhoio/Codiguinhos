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
    pygame.draw.line( tela, preto, (0, 600), (800, 0))
    pygame.draw.circle( tela, preto, (400, 300), 100)
    pygame.draw.circle( tela, branco, (400, 300), 95)
    pygame.display.update()
pygame.quit()