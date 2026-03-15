import pygame
import math


LARGO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (180, 180, 180)
ROJO = (255, 0, 0)
FPS = 60
GROSOR = 5
PADDING = 20


pygame.init()
pantalla = pygame.display.set_mode((LARGO, ALTO))
pygame.display.set_caption("Nombre del proyecto")
reloj = pygame.time.Clock()
theta = math.pi / 6
d_theta = 0.1


def traducir(coordenadas, escala=LARGO // 2):
    ESCALA = escala - (2 * PADDING)
    x, y = coordenadas
    x_pantalla = PADDING + (x * ESCALA)
    y_pantalla = (ALTO - PADDING) - (y * ESCALA)

    return (int(x_pantalla), int(y_pantalla))


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                pygame.quit()
                exit()
        elif evento.type == pygame.MOUSEWHEEL:
            if evento.y >= 1:
                d_theta *= 1.01
            else:
                d_theta *= 0.99

    # RENDER
    pantalla.fill(BLANCO)
    T = math.tan(theta)
    A = (1, T)
    B = (0, 0)
    C = (1, 0)

    d_T = math.tan(theta + d_theta) - T

    D = (1, T + d_T)

    L = math.sqrt(1**2 + T**2)

    L_d_theta = d_T * math.cos(theta)

    angulo = math.pi / 2 + theta
    E = (A[0] + math.cos(angulo) * L_d_theta, A[1] + math.sin(angulo) * L_d_theta)

    pygame.draw.polygon(pantalla, NEGRO, list(map(traducir, (A, B, C))), GROSOR)

    pygame.draw.line(pantalla, GRIS, traducir(B), traducir(D), GROSOR)
    pygame.draw.polygon(pantalla, NEGRO, list(map(traducir, (A, D, E))))

    inicio, fin = 0, math.pi / 2
    num = 100
    step = (fin - inicio) / num
    for angulo in [inicio + step * i for i in range(num)]:
        x = L * math.cos(angulo)
        y = L * math.sin(angulo)
        pygame.draw.aacircle(pantalla, NEGRO, traducir((x, y)), 1)

    pygame.display.flip()

    reloj.tick(FPS)
