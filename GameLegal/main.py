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
    pygame.draw.circle( tela, preto, (300, 300), 50) # largura, altura e raio
    pygame.draw.circle( tela, preto, (400, 300), 50) #
    pygame.draw.line( tela, preto, (350,300), (350,0), 10)
    pygame.display.update()
pygame.quit()