import pygame
import sys

pygame.init()

# Tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Genio Quiz")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 0, 200)

fonte = pygame.font.SysFont("arial", 28)

estado = "menu"
fase = 1


def texto(txt, x, y, cor=BRANCO):
    render = fonte.render(txt, True, cor)
    tela.blit(render, (x, y))


def botao(texto_btn, x, y, w, h, cor, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(tela, cor, (x, y, w, h))

    texto_render = fonte.render(texto_btn, True, PRETO)
    tela.blit(texto_render, (x + 20, y + 15))

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        if click[0] == 1 and acao:
            pygame.time.delay(200)
            acao()


def game_over():
    global estado
    estado = "gameover"


def proxima_fase():
    global fase, estado
    fase += 1
    estado = "jogo"


def vitoria():
    global estado
    estado = "vitoria"


# Fases (Gênio Quiz estilo troll)
def fase_jogo():
    global estado

    tela.fill(PRETO)

    if fase == 1:
        texto("Fase 1: Quanto é 2 + 2?", 200, 100)
        botao("4", 100, 200, 200, 60, VERDE, game_over)
        botao("22", 100, 300, 200, 60, VERMELHO, game_over)
        botao("5", 100, 400, 200, 60, AZUL, proxima_fase)

    elif fase == 2:
        texto("Fase 2: Clique no botão vermelho", 200, 100)
        botao("Azul 😏", 100, 200, 200, 60, AZUL, game_over)
        botao("Verde 😏", 100, 300, 200, 60, VERDE, game_over)
        botao("Isso aqui é vermelho", 100, 400, 300, 60, VERMELHO, proxima_fase)

    elif fase == 3:
        texto("Fase 3: Não clique em nada", 200, 100)

        # pegadinha clássica: clicar = perde
        botao("CLIQUE AQUI", 250, 300, 250, 80, AZUL, game_over)

        # vitória escondida
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            vitoria()


def menu():
    tela.fill(PRETO)
    texto("GENIO QUIZ", 300, 150)
    botao("Jogar", 300, 300, 200, 60, VERDE, lambda: set_estado_jogo())


def set_estado_jogo():
    global estado
    estado = "jogo"


def tela_game_over():
    tela.fill(PRETO)
    texto("💀 GAME OVER 💀", 280, 250)
    texto("Clique para voltar", 250, 350)

    if pygame.mouse.get_pressed()[0]:
        reset()


def tela_vitoria():
    tela.fill(PRETO)
    texto("🏆 VOCÊ VENCEU 🏆", 250, 250)


def reset():
    global estado, fase
    estado = "menu"
    fase = 1


# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if estado == "menu":
        menu()

    elif estado == "jogo":
        fase_jogo()

    elif estado == "gameover":
        tela_game_over()

    elif estado == "vitoria":
        tela_vitoria()

    pygame.display.update()