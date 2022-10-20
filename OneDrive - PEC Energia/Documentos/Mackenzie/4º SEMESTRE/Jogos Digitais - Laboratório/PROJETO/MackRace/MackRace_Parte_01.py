from pickle import FALSE
import pygame

pygame.init()
x = 350
y = 400
v = 10
y1 = -50
v1 = -20

fundo = pygame.image.load('pista.jpg')
pista1 = pygame.image.load('pista3.png')
pista2 = pygame.image.load('pista4.png')
carro = pygame.image.load('carro.png')
janela = pygame.display.set_mode((800,650))
pygame.display.set_caption('Jogo parte 1')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = FALSE
    comandos = pygame.key.get_pressed()
    if comandos [pygame.K_UP]:
        y -= v
    if comandos [pygame.K_DOWN]:
        y += v
    if comandos [pygame.K_RIGHT]:
        y += v
    if comandos [pygame.K_LEFT]:
        y -= v
    y1 -= v1
    if (y1 >= 700):
        y1 =- 50
    janela.blit(fundo, (0,0))
    janela.blit(pista1, (306, y1))
    janela.blit(pista2, (496, y1))
    janela.blit(carro, (x,y))
    pygame.display.update()
pygame.quit()


