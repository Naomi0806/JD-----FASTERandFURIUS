from pickle import FALSE
from random import randint
import time
import pygame
import math
pygame.init()

x = 470
y = 500
v = 20

v1 = -25
y1 = -25

v2 = -20
y2 = randint(-800, -600)

v3 = -20
y3 = randint(-1600, -1200)

v4 = -20
y4 = randint(-3000, -1800)

timer = 0
start_timestamp = time.time()
seconds = 0
nivel = 1

fundo = pygame.image.load('imagens/estrada.jpeg')
pista1 = pygame.image.load('imagens/movimento.jpeg')
pista2 = pygame.image.load('imagens/movimento.jpeg')
samu = pygame.image.load('imagens/ambulancia.png')
moto = pygame.image.load('imagens/moto.png')
carro2 = pygame.image.load('imagens/carro2.png')
carro = pygame.image.load('imagens/carro.png')
janela = pygame.display.set_mode((1000,782))
pygame.display.set_caption('Jogo parte 1')

font = pygame.font.SysFont('arial', 30)
texto = font.render('Tempo:   ', True, (0, 0, 0), (255,255,0))
texto_nivel = font.render(f'Nível: {nivel}', True, (0, 0, 0), (255,255,0))
pos_texto = texto.get_rect()
post_text_nivel = texto_nivel.get_rect()
pos_texto.center = (65, 50)
post_text_nivel = (5, 90)

janela_aberta = True

game_velocidade = 50
while janela_aberta:
    pygame.time.delay(game_velocidade)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
    comandos = pygame.key.get_pressed()

    if comandos [pygame.K_RIGHT] and x <= 750:
        x += v
    if comandos [pygame.K_LEFT] and x >= 155:
        x -= v
        
    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4
    
    if (y1 >= 842):
        y1 =- 25
    if (y2 >= 800):
        y2 = randint(-800, -600)
    if (y3 >= 1200):
        y3 = randint(-1600, -1200)
    if (y4 >= 1800):
        y4 = randint(-3000, -1800)

    # Aumente esse intervalo para abaixar a probabilidade de os carros virem juntos    
    if(200 <= (y2 - y3) <= -270):
        y4 =  randint(-4000, -3800)
    
    # Colisões
    if(x >= 610 and -10 <= (y - y4) <= 30):
        janela_aberta = False
    if(370 <= x <= 470 and -10 <= (y - y3) <= 30):
        janela_aberta = False
    if(x <= 330 and -10 <= (y - y2) <= 30):
        janela_aberta = False

    if(seconds >= 20):
        game_velocidade = 30
        nivel = 2
    if(seconds >= 40):
        game_velocidade = 20
        nivel = 3
    if(seconds >= 60):
        game_velocidade = 10
        nivel = 4
    if(seconds >= 80):
        game_velocidade = 7
        nivel = 5

    if (timer < 20):
        timer += 1
    else:
        texto = font.render(' Tempo: ' + str(math.floor(((time.time() - start_timestamp) - 0.7))) + " ", True, (0, 0, 0), (255,255,0))
        seconds += 1
        texto_nivel = font.render(f'Nível {nivel}', True, (0, 0, 0), (255,255,0))
        timer = 0
        
    janela.blit(fundo, (0,0))
    janela.blit(pista1, (370, y1))
    janela.blit(pista2, (610, y1))
    janela.blit(samu, (655, y4))
    janela.blit(moto, (470, y3))
    janela.blit(carro2, (120, y2))
    janela.blit(carro, (x,y))
    janela.blit(texto, pos_texto)
    janela.blit(texto_nivel, post_text_nivel)
    pygame.display.update()

pygame.quit()