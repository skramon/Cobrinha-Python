import pygame
import sys

pygame.init()

# Tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

clock = pygame.time.Clock()

# Cobra
tamanho_bloco = 20
cobra = [[100, 50], [80, 50], [60, 50]]
direcao = "DIREITA"

def desenhar_cobra():
    for parte in cobra:
        pygame.draw.rect(
            tela,
            VERDE,
            pygame.Rect(parte[0], parte[1], tamanho_bloco, tamanho_bloco)
        )

def mover_cobra():
    if direcao == "DIREITA":
        nova_cabeca = [cobra[0][0] + tamanho_bloco, cobra[0][1]]
    elif direcao == "ESQUERDA":
        nova_cabeca = [cobra[0][0] - tamanho_bloco, cobra[0][1]]
    elif direcao == "CIMA":
        nova_cabeca = [cobra[0][0], cobra[0][1] - tamanho_bloco]
    elif direcao == "BAIXO":
        nova_cabeca = [cobra[0][0], cobra[0][1] + tamanho_bloco]

    cobra.insert(0, nova_cabeca)
    cobra.pop()

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT and direcao != "ESQUERDA":
                direcao = "DIREITA"
            elif evento.key == pygame.K_LEFT and direcao != "DIREITA":
                direcao = "ESQUERDA"
            elif evento.key == pygame.K_UP and direcao != "BAIXO":
                direcao = "CIMA"
            elif evento.key == pygame.K_DOWN and direcao != "CIMA":
                direcao = "BAIXO"

    mover_cobra()
    tela.fill(PRETO)
    desenhar_cobra()
    pygame.display.update()
    clock.tick(10)
