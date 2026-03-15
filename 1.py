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


def traducir(coordenadas):
    ESCALA = LARGO - (2 * PADDING)
    x, y = coordenadas
    x_pantalla = PADDING + (x * ESCALA)
    y_pantalla = (ALTO - PADDING) - (y * ESCALA)

    return (int(x_pantalla), int(y_pantalla))


def dibujar_triangulo_recto(pantalla: pygame.Surface, theta: float):
    """
    Si llamamos a=cateto adyacente ,b=cateto opuesto sabemos que h = hipotenusa
    cos(theta) = a/h y sin(theta) = b/h
    entonces tan(theta) = sin(theta)/cos(theta) = (b/h) / (a/h) = b/a

    Sabemos que a = 1 por lo que T = tan(theta) = b
    """


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

    pygame.display.flip()

    reloj.tick(FPS)
