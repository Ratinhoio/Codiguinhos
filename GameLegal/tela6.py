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
    pygame.draw.line( tela, preto, (100, 100), (250, 500), 5) #Linha
    pygame.draw.line( tela, preto, (250, 500), (450, 335), 5) #Linha
    pygame.draw.line( tela, preto, (450, 300), (700, 300), 5) #Linha
    pygame.draw.circle( tela, preto, (100, 100), 50)
    pygame.draw.circle( tela, branco, (100, 100), 45)
    pygame.draw.circle( tela, preto, (250, 500), 50)
    pygame.draw.circle( tela, branco, (250, 500), 45)
    pygame.draw.circle( tela, preto, (450, 300), 50)
    pygame.draw.circle( tela, branco, (450, 300), 45)
    pygame.draw.circle( tela, preto, (700, 300), 50)
    pygame.draw.circle( tela, branco, (700, 300), 45, )
    pygame.display.update()
pygame.quit()