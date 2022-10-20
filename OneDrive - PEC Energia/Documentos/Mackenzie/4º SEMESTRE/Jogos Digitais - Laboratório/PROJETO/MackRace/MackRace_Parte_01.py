from pickle import FALSE
import pygame
pygame.init()
x = 400
y = 600
v = 10
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro.png')
janela = pygame.display.set_mode((800,650))
pygame.display.set_caption('Jogo parte 1')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = FALSE
comandos = pygame .key.get_pressed()
if comandos [pygame.K_UP]:
    y- = v
if comandos [pygame.K_DOWN]:
    y- = v
if comandos [pygame.K_RIGHT]:
    y- = 
if comandos [pygame.K_LEFT]:
    y- = 
    janela.blit(fundo,(0,0))
    carro.blit(carro(x,y))
    pygame.display.update()
pygame.quit()


