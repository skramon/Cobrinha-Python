#importação de bibliotecas
import pygame
import sys

pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set-mode((LARGURA, ALTURA)) #cria a janela de exibição
pygame.display.set-capturation("Jogo da Cobrinha") #define um titulo para a janela

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

clock = pygame.time.Clock() # controla a taxa de atualização da tela (fps)

#configurações da cobrinha
tamanho_bloco = 20
cobra = [[100,50], [80,50], [60,50]] #lista que armazena as posições da cobrinha
direcao = "DIREITA" #direção inicial da cobrinha
