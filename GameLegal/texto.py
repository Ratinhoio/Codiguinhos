import pygame, time, os
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
rodando = True
fonte = pygame.font.SysFont(None, 20)
imagem = pygame.image.load("shrek.jpg")
imagem = pygame.transform.scale(imagem, (800, 600))
imagem = pygame.transform.rotate(imagem, 0)
fps = pygame.time.Clock()
os.system('cls')
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(120)
    texto = fonte.render("bao?", True, preto)
    tela.blit(imagem, (0,0))
    tela.blit(texto, (380, 300))
    pygame.display.update()
pygame.quit()
