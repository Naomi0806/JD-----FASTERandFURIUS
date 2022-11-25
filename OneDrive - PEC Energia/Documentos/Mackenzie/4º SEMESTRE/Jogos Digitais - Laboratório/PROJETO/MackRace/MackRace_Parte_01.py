# from pickle import FALSE
# from random import randint
# import pygame
# pygame.init()

# x = 470
# y = 500
# v = 20

# v1 = -25
# y1 = -25

# v2 = -20
# y2 = -20

# v3 = -20
# y3 = -30

# v4 = -20
# y4 = -25

# timer = 0
# seconds = 0

# fundo = pygame.image.load('imagens/estrada.jpeg')
# pista1 = pygame.image.load('imagens/movimento.jpeg')
# pista2 = pygame.image.load('imagens/movimento.jpeg')
# samu = pygame.image.load('imagens/ambulancia.png')
# moto = pygame.image.load('imagens/moto.png')
# carro2 = pygame.image.load('imagens/carro2.png')
# carro = pygame.image.load('imagens/carro.png')
# janela = pygame.display.set_mode((1000,782))
# pygame.display.set_caption('Jogo parte 1')

# font = pygame.font.SysFont('arial', 30)
# texto = font.render('Tempo:   ', True, (0, 0, 0), (255,255,0))
# pos_texto = texto.get_rect()
# pos_texto.center = (65, 50)

# janela_aberta = True
# while janela_aberta:
#     pygame.time.delay(50)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             janela_aberta = False
            
#     comandos = pygame.key.get_pressed()
# #    if comandos [pygame.K_UP]:
# #        y -= v
# #    if comandos [pygame.K_DOWN]:
# #        y += v
#     if comandos [pygame.K_RIGHT] and x <= 750:
#         x += v
#     if comandos [pygame.K_LEFT] and x >= 155:
#         x -= v
        
#     y1 -= v1
#     y2 -= v2
#     y3 -= v3
#     y4 -= v4
    
#     if (y1 >= 842):
#         y1 =- 25
#     if (y2 >= 884):
#         y2 = randint(-300, -250)
#     if (y3 >= 920):
#         y3 = randint(-100, -50)
#     if (y4 >= 800):
#         y4 = randint(-500, -450)
        
#     if (timer < 20):
#         timer += 1
#     else:
#         seconds += 1
#         texto = font.render(' Tempo: ' + str(seconds) + " ", True, (0, 0, 0), (255,255,0))
#         timer = 0
        
#     janela.blit(fundo, (0,0))
#     janela.blit(pista1, (370, y1))
#     janela.blit(pista2, (610, y1))
#     janela.blit(samu, (615, y4))
#     janela.blit(moto, (415, y3))
#     janela.blit(carro2, (95, y2))
#     janela.blit(carro, (x,y))
#     janela.blit(texto, pos_texto)
#     pygame.display.update()

# pygame.quit()

from pickle import FALSE
from random import randint
import pygame
import math
pygame.init()

font = pygame.font.SysFont('arial', 30)

def mensagem_padrao():
    texto = font.render('GAME OVER', True, (0, 0, 0), (255,255,0))
    pos_texto = texto.get_rect()
    pos_texto.center = (300, 100)
    janela.blit(texto, pos_texto)


x = 470
y = 350
v = 20

v1 = -25
y1 = -20

v2 = -17
y2 = -500
x2 = 130

v3 = -25
y3 = -300

v4 = -25
y4 = -700
x4 = 655

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

texto2 = font.render('Tempo:   ', True, (0, 0, 0), (255,255,0))
pos_texto2 = texto2.get_rect()
pos_texto2.center = (65, 50)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
    comandos = pygame.key.get_pressed()

    if comandos [pygame.K_RIGHT] and x <= 735:
        x += v
    if comandos [pygame.K_LEFT] and x >= 155:
        x -= v

    if(x >= 610 and -10 <= (y - y4) <= 30):
        pygame.quit()
        mensagem_padrao()

    if(370 <= x <= 470 and -10 <= (y - y3) <= 30):
        y = 1200
        mensagem_padrao()

    if(x <= 330 and -10 <= (y - y2) <= 30):
        y = 1200
        mensagem_padrao()


    # if (x + 40 > x4 and y + 180 > y4):
    #      y = 1200

    # if (x - 150 < x2 and y + 235 > y2):
    #      y = 1200
    # #                                                          #posx    
    # if (x + 20 > 435 and y + 250 > y3)and(x - (-20) < 435 and y + 250 > y3):
    #       y = 1200
        
    y1 -= v1
    y2 -= v2
    y3 -= v3
    y4 -= v4

    if (y1 >= 842):
        y1 =- 25

    if (y2 >= 884):
        y2 = randint(-800, -300)

    if (y3 >= 920):
        y3 = randint(-800, -300)

    if (y4 >= 800): 

        if math.fabs(y3 - y2) > 720:
            y4 = randint(-650, -400)
        
        if math.fabs(y3 - y2) < 720:
            if y3 < y2:
                y4 = y3 - 800

            else:
                y4 = y2 -800  
        

    # class SPRITESA (pygame.sprite.Sprite):
    #     def __init__(self):
    #         pygame.sprite.Sprite.__init__(self)
    #         maskcarro2 = pygame.mask.from_surface(carro2) 
    #         selfrectcarro2 = maskcarro2.get_rect()       
    #         masksamu = pygame.mask.from_surface(samu)
    #         selfrectsamu = masksamu.get_rect()
    #         maskmoto = pygame.mask.from_surface(moto)
    #         selfrectmoto = maskmoto.get_rect()


    # NEWCLASS = SPRITESA()
    # maskcarro1 = pygame.mask.from_surface(carro)
    # selfrectcarro1 = maskcarro1.get_rect()
    # grupo_sprite = pygame.sprite.Group()
    # grupo_sprite.add(NEWCLASS)

    # colisoes = pygame.sprite.spritecollide(maskcarro1,grupo_sprite,FALSE)

    # if colisoes:
    #     y = 1200

    if (timer < 20):
        timer += 1
    else:
        seconds += 1
        texto2 = font.render(' Tempo: ' + str(seconds) + " ", True, (0, 0, 0), (255,255,0))
        timer = 0
        
    janela.blit(fundo, (0, 0))
    janela.blit(pista1, (370, y1))
    janela.blit(pista2, (610, y1))
    janela.blit(samu, (x4, y4))
    janela.blit(moto, (435, y3))
    janela.blit(carro2, (x2, y2))
    janela.blit(carro, (x,y))
    janela.blit(texto2, pos_texto2)
 
    pygame.display.update()

pygame.quit()