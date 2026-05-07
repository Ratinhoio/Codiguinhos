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
    pygame.draw.line( tela, preto, (0, 300), (800, 300 ))
    pygame.draw.line( tela, preto, (100, 450), (100, 50 ))
    pygame.draw.line( tela, preto, (100, 50), (150, 350))
    pygame.draw.line( tela, preto, (200, 100), (150, 350))
    pygame.draw.line( tela, preto, (200, 450), (200, 100 ))
    pygame.draw.line( tela, preto, (200, 450), (400, 50))
    pygame.draw.line( tela, preto, (400, 50), (700, 400))
    pygame.display.update()
pygame.quit()