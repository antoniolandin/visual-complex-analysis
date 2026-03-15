"""
Introduction 9
1.5 A complex number can be interpreted as a rotation and expansion of the plane
"""

import pygame
import math

LARGO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
FPS = 60
RADIO = 20

pygame.init()
pantalla = pygame.display.set_mode((LARGO, ALTO))
pygame.display.set_caption("Interpretación complejos")
reloj = pygame.time.Clock()

c = 1 / math.sqrt(2) + (1 / math.sqrt(2)) * 1j


def traducir_complejo(z: complex):
    return (z.real * LARGO, ALTO - z.imag * ALTO)


def traducir_pixel(pixel: tuple[int, int]):
    return (pixel[0] / LARGO) + (1 - (pixel[1] / ALTO)) * 1j


complejos = []

transformar = False


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                pygame.quit()
                exit()
            if evento.key == pygame.K_SPACE:
                transformar = not transformar
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == pygame.BUTTON_LEFT:
                complejos.append(traducir_pixel(pygame.mouse.get_pos()))

    # RENDER
    pantalla.fill(BLANCO)
    for complejo in complejos:
        if transformar:
            complejo *= c
        pygame.draw.aacircle(pantalla, NEGRO, traducir_complejo(complejo), RADIO)

    if len(complejos) > 2:
        pygame.draw.polygon(
            pantalla,
            NEGRO,
            [traducir_complejo(z * c if transformar else 1) for z in complejos],
        )

    pygame.draw.circle(pantalla, VERDE, traducir_complejo(c), RADIO)

    pygame.display.flip()

    reloj.tick(FPS)
