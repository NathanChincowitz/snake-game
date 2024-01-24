import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###
    

#config inicial
import random
import pygame

pygame.init()
pygame.display.set_caption('jogo snake python')
largura, altura = 600, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
direcao_y = 0
direcao_x = 0

#cores RGB
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

#parametros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 10


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, red, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, white, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", True, green)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    global direcao_x, direcao_y

#baixo
    if tecla == pygame.K_DOWN and direcao_y == -tamanho_quadrado:
        direcao_x = 0
        direcao_y = -tamanho_quadrado

    elif tecla == pygame.K_DOWN:
        direcao_x = 0
        direcao_y = tamanho_quadrado

#cima
    if tecla == pygame.K_UP and direcao_y == tamanho_quadrado:
        direcao_x = 0
        direcao_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        direcao_x = 0
        direcao_y = -tamanho_quadrado

#direita
    if tecla == pygame.K_RIGHT and direcao_x == -tamanho_quadrado:
        direcao_x = -tamanho_quadrado
        direcao_y = 0
    elif tecla == pygame.K_RIGHT:
        direcao_x = tamanho_quadrado
        direcao_y = 0
#esquerda        
    if tecla == pygame.K_LEFT and direcao_x == tamanho_quadrado:
        direcao_x = tamanho_quadrado    
        direcao_y = 0
    elif tecla == pygame.K_LEFT:
        direcao_x = -tamanho_quadrado
        direcao_y = 0

    return direcao_x, direcao_y

def rodar_jogo():
    fim_jogo = False
    

    x = largura / 2
    y = altura / 2
    
    global direcao_x, direcao_y
    
    tamanho_cobra = 1
    pixels = [] 
    
    comida_x, comida_y = gerar_comida()
    
    #criar loop infinito
    while not fim_jogo:
        tela.fill(black)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
                
            elif evento.type == pygame.KEYDOWN:
                direcao_x, direcao_y = selecionar_velocidade(evento.key)

            
        # desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posição da cobra
        if x < 0 or y < 0 or x >= largura or y >= altura:
            fim_jogo = True
        
        x += direcao_x
        y += direcao_y
        
        # desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)
            
        # desenhar pontuação
        desenhar_pontuacao(tamanho_cobra - 1)
   
        # atualização da tela
        pygame.display.update()
        
        #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
            global velocidade_jogo
            velocidade_jogo += 2

        relogio.tick(velocidade_jogo)


rodar_jogo()
