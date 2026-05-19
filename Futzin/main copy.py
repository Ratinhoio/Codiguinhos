import pygame, time, random, os
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
rodando = True
fonte = pygame.font.SysFont("arial", 20)
xBola = 400
yBola = 300
rBola = 50
xBola2 = random.randint (50, 750)
yBola2 = random.randint (50, 550)
imagem = pygame.image.load("Bola2.png")
imagem = pygame.transform.scale(imagem, (20, 20))
imagem = pygame.transform.rotate(imagem, 0)
campo = pygame.image.load("Campo.jpg")
campo = pygame.transform.scale(campo, (800, 600))
pygame.mixer.music.load("")
pygame.mixer.muisc.play(-1) #Looping infinito
fps = pygame.time.Clock()
while rodando:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(branco)
    fps.tick(60)
    tela.blit(campo, (0,0))

  
    tela.blit(imagem, (xBola,yBola))
    pygame.key.get_pressed()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE]:
        break
    if teclas[pygame.K_d]:
        xBola += 15
    if teclas[pygame.K_a]:
        xBola -= 15
    if teclas[pygame.K_s]:
        yBola += 15
    if teclas[pygame.K_w]:
        yBola -= 15
    if xBola >= 780:
        xBola = 780
    elif xBola <= 0:
        xBola = 0
    elif yBola >= 600:
        yBola = 600
    elif yBola <= 0:
        yBola = 0
    if xBola > 700 and yBola > 250 and yBola < 350:
        texto = fonte.render("GOLLLLLLL", True, preto)
    texto = fonte.render(f"Posiçao: x = {xBola} e y = {yBola}",  True, branco)
    tela.blit(texto, (10,10))
    pygame.display.update()
pygame.quit()