import pygame
import sys
import random

# -----------------------------------
# CONFIGURACIÓN BÁSICA
# -----------------------------------
ANCHO = 800
ALTO = 600
FPS = 30

COLOR_FONDO = (25, 25, 60)
COLOR_BLANCO = (255, 255, 255)
COLOR_AZUL = (0, 120, 255)
COLOR_VERDE = (0, 200, 0)
COLOR_ROJO = (200, 0, 0)

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inglés Básico - Colores")
clock = pygame.time.Clock()

fuente_titulo = pygame.font.SysFont("arial", 48, bold=True)
fuente_texto = pygame.font.SysFont("arial", 30)
fuente_pequena = pygame.font.SysFont("arial", 22)

# -----------------------------------
# PREGUNTAS: COLORES
# es = español, en = respuesta correcta
# -----------------------------------
PREGUNTAS = [
    {"es": "rojo",     "en": "red",    "opciones": ["red", "blue", "green"]},
    {"es": "azul",     "en": "blue",   "opciones": ["yellow", "blue", "black"]},
    {"es": "verde",    "en": "green",  "opciones": ["white", "green", "orange"]},
    {"es": "amarillo", "en": "yellow", "opciones": ["brown", "purple", "yellow"]},
    {"es": "negro",    "en": "black",  "opciones": ["black", "pink", "grey"]},
    {"es": "blanco",   "en": "white",  "opciones": ["red", "white", "blue"]},
]

# -----------------------------------
# FUNCIONES DE APOYO
# -----------------------------------
def dibujar_texto(surface, texto, fuente, color, centro):
    """Dibuja texto centrado en la posición indicada."""
    imagen = fuente.render(texto, True, color)
    rect = imagen.get_rect(center=centro)
    surface.blit(imagen, rect)

def crear_botones(opciones):
    """Crea los botones (rectángulos) para las opciones."""
    botones = []
    ancho = 400
    alto = 60
    x = (ANCHO - ancho) // 2
    inicio_y = 250
    espacio_y = 90

    for i, opcion in enumerate(opciones):
        rect = pygame.Rect(x, inicio_y + i * espacio_y, ancho, alto)
        botones.append((rect, opcion))
    return botones

def dibujar_boton(rect, texto):
    """Dibuja un botón con texto."""
    pygame.draw.rect(pantalla, COLOR_AZUL, rect, border_radius=10)
    pygame.draw.rect(pantalla, COLOR_BLANCO, rect, 2, border_radius=10)
    dibujar_texto(pantalla, texto, fuente_texto, COLOR_BLANCO, rect.center)

# -----------------------------------
# JUEGO PRINCIPAL
# -----------------------------------
def juego_colores():
    preguntas = PREGUNTAS.copy()
    random.shuffle(preguntas)
    indice = 0
    puntaje = 0
    mensaje = ""
    color_mensaje = COLOR_BLANCO

    # preparar primera pregunta
    pregunta_actual = preguntas[indice]
    opciones = pregunta_actual["opciones"][:]
    random.shuffle(opciones)
    botones = crear_botones(opciones)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mx, my = pygame.mouse.get_pos()
                for rect, opcion in botones:
                    if rect.collidepoint(mx, my):
                        # comprobar respuesta
                        if opcion == pregunta_actual["en"]:
                            mensaje = "¡Correcto!"
                            color_mensaje = COLOR_VERDE
                            puntaje += 1
                        else:
                            mensaje = f"Incorrecto. '{pregunta_actual['es']}' es '{pregunta_actual['en']}'"
                            color_mensaje = COLOR_ROJO

                        # siguiente pregunta
                        indice += 1
                        if indice >= len(preguntas):
                            ejecutando = False
                        else:
                            pregunta_actual = preguntas[indice]
                            opciones = pregunta_actual["opciones"][:]
                            random.shuffle(opciones)
                            botones = crear_botones(opciones)
                        break

        # DIBUJAR PANTALLA
        pantalla.fill(COLOR_FONDO)

        dibujar_texto(
            pantalla,
            "Aprendamos los colores en inglés",
            fuente_titulo,
            COLOR_BLANCO,
            (ANCHO // 2, 80),
        )

        if ejecutando:
            texto_preg = f"¿Cómo se dice '{pregunta_actual['es']}' en inglés?"
            dibujar_texto(pantalla, texto_preg, fuente_texto, COLOR_BLANCO, (ANCHO // 2, 170))

            for rect, opcion in botones:
                dibujar_boton(rect, opcion)

            dibujar_texto(pantalla, f"Puntaje: {puntaje}", fuente_pequena, COLOR_BLANCO, (100, 30))

            if mensaje:
                dibujar_texto(pantalla, mensaje, fuente_pequena, color_mensaje, (ANCHO // 2, 540))
        else:
            # pantalla final
            dibujar_texto(pantalla, "¡Juego terminado!", fuente_titulo, COLOR_BLANCO, (ANCHO // 2, 200))
            dibujar_texto(
                pantalla,
                f"Tu puntaje fue: {puntaje} de {len(preguntas)}",
                fuente_texto,
                COLOR_BLANCO,
                (ANCHO // 2, 280),
            )
            dibujar_texto(
                pantalla,
                "Cierra la ventana para salir.",
                fuente_pequena,
                COLOR_BLANCO,
                (ANCHO // 2, 360),
            )

        pygame.display.flip()
        clock.tick(FPS)

# -----------------------------------
# PUNTO DE ENTRADA
# -----------------------------------
if __name__ == "__main__":
    juego_colores()
