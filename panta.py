# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

class protectordepantalla(Sprite):

    def __init__(self):
        self.image = pygame.image.load("imagenes/puntero.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(0, 0)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            pygame.quit()
		


def p():
    salir = False

    # creacion de la ventana
    screen = pygame.display.set_mode((640, 480),pygame.FULLSCREEN)
    pygame.display.set_caption("Protector de Pantalla")
    fondo = pygame.image.load("imagenes/ubuntufinal.png").convert()
    logotipo = pygame.image.load("imagenes/logo.png").convert_alpha()
    fondo.blit(logotipo, (500, 340))


    # objetos
    temporizador = pygame.time.Clock()
    protege = protectordepantalla()

    while not salir:
        protege.update()

        # actualizacion grafica
        screen.blit(fondo, (30, 10))
        screen.blit(protege.image, protege.rect)
        pygame.display.flip()

        temporizador.tick(10)
        # gestion de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True


