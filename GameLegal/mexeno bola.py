import pygame, time, os
pygame.init()
largura = 800
altura = 600
tela = pygame.display.set_mode( (largura, altura) )
pygame.display.set_caption("Meu joguinhoooo")
preto = (0,0,0)
branco = (255, 255, 255)
rodando = True
ino = True
deceno = False 
xBola = 400
yBola = 300
xBarra = 400
yBarra = 100
xBarra2 = 400
yBarra2 = 500
mult = 1
pontuaçao = 0
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
    tela.blit(imagem, (0,0))
    pygame.draw.rect(tela, preto, (xBarra,yBarra,100,10))
    pygame.draw.rect(tela, preto, (xBarra2,yBarra2,100,10))
    pygame.draw.circle( tela, preto, (xBola, yBola), 20) # largura, altura e raio
    if xBola - 20 <= 0:
        ino = True
    elif xBola + 20 >= 800:
        ino = False
    if ino:
        xBola += 2 * mult
    else:
        xBola -= 2 * mult
        
    if yBola - 20 <= 0:
        print("Jogador 1 Ganhou!")
        break
        deceno = True
    elif yBola + 20 >= 600:
        print("Jogador 2 Ganhou!")
        break
        deceno = False
    elif yBola - 20 <= yBarra + 10 and yBola + 20 >= yBarra and xBola >= xBarra and xBola <= xBarra + 100:
        deceno = True
        yBola = yBarra + 31
        pontuaçao += 1
        mult += 0.1 
    elif yBola + 20 >= yBarra2 and yBola - 20 <= yBarra2 + 10 and xBola >= xBarra2 and xBola <= xBarra2 + 100:
        deceno = False
        pontuaçao += 1
        yBola = yBarra2 - 31
        mult += 0.1 
    if deceno:
        yBola += 2 * mult
    else:
        yBola -= 2 * mult
    
    pygame.key.get_pressed()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a]:
        xBarra -= 10
    if teclas[pygame.K_d]:
        xBarra += 10
    if xBarra <= 0:
        xBarra += 10
    elif xBarra >= 700:
        xBarra -= 10
    if teclas[pygame.K_LEFT]:
        xBarra2 -= 10
    if teclas[pygame.K_RIGHT]:
        xBarra2 += 10
    if xBarra2 <= 0:
        xBarra2 += 10
    elif xBarra2 >= 700:
        xBarra2 -= 10
    pygame.display.update()
time.sleep(1.5)
pygame.quit()
time.sleep(2)
os.system('cls')
print(f"Sua pontuação foi de {pontuaçao} pontos!")
time.sleep(2)