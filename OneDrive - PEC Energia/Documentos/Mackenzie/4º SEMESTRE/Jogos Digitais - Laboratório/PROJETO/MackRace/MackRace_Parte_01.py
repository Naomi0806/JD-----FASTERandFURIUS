from pickle import FALSE
from random import randint
import pygame
pygame.init()

x = 470
y = 500
v = 20

v1 = -25
y1 = -25

v2 = -20
y2 = -20

v3 = -20
y3 = -30

v4 = -20
y4 = -25

timer = 0
seconds = 0

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
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
    comandos = pygame.key.get_pressed()
#    if comandos [pygame.K_UP]:
#        y -= v
#    if comandos [pygame.K_DOWN]:
#        y += v
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
    if (y2 >= 884):
        y2 = randint(-300, -250)
    if (y3 >= 920):
        y3 = randint(-100, -50)
    if (y4 >= 800):
        y4 = randint(-500, -450)
        
    if (timer < 20):
        timer += 1
    else:
        seconds += 1
        texto = font.render(' Tempo: ' + str(seconds) + " ", True, (0, 0, 0), (255,255,0))
        timer = 0
        
    janela.blit(fundo, (0,0))
    janela.blit(pista1, (370, y1))
    janela.blit(pista2, (610, y1))
    janela.blit(samu, (615, y4))
    janela.blit(moto, (415, y3))
    janela.blit(carro2, (95, y2))
    janela.blit(carro, (x,y))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()