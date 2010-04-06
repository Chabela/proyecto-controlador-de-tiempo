import time
import pygame
from pygame.locals import *


class protectordepantalla:
    def __init__(self):
        self.imagen = pygame.image.load("imagenes/logo.png").convert_alpha()
        self.ver = self.imagen.get_rect()
        self.ver.move_ip(100,100)
    def tecla(self):
        self.teclas=pygame.key.get_pressed()
        if self.teclas[K_SPACE]:
            pygame.quit()

        


salir=False
protectores = pygame.display.set_mode((560,840),pygame.FULLSCREEN)
pygame.display.set_caption('Protector de pantallas')

#cargamos una imagen
#convertimo (convert_alpha) la superficie creada por load a u formato de color que permite imprimirrla mucho mas rapidas sobre la pantalla
logotipo=pygame.image.load('imagenes/ubuntu.PNG').convert_alpha()
protectores.blit(logotipo,(0,0))
#se muestra los cambios en la pantalla
pygame.display.flip()

# objetos
temporizador = pygame.time.Clock()
protectores = protectordepantalla()

while not salir:
    protectordepantalla.tecla()

    # actualizacion grafica
    protectores.blit(fondo, (0, 0))
    protectores.blit(protectores.imagen, protectores.ver)
    pygame.display.flip()

    temporizador.tick(60)
    # gestion de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salir = True

protecto()
#esperemos que cierre la ventana
pygame.event.set_allowed(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.wait()
