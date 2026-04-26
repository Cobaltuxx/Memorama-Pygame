import pygame
import random

pygame.init()
ventana = pygame.display.set_mode((460, 460))
fuente = pygame.font.SysFont("Arial", 25)

colores = [(200,0,0), (0,200,0), (0,0,200), (255,255,0), (255,0,255), (0,255,255), (255,128,0), (128,0,255)] * 2
random.shuffle(colores)

mostradas = [False] * 16
elegidas = []
parejas_logradas = 0

jugando = True
while jugando:
    ventana.fill((30, 30, 30)) 
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN and len(elegidas) < 2:
            x, y = pygame.mouse.get_pos()
            col = x // 115
            fila = y // 115
            indice = fila * 4 + col
            
            if not mostradas[indice]:
                mostradas[indice] = True
                elegidas.append(indice)

    for i in range(16):
        x = (i % 4) * 115 + 10
        y = (i // 4) * 115 + 10
        
        color_rect = colores[i] if mostradas[i] else (100, 100, 100)
        pygame.draw.rect(ventana, color_rect, (x, y, 100, 100))

    pygame.display.flip()

    if len(elegidas) == 2:
        pygame.time.wait(500) 
        i1, i2 = elegidas
        
        if colores[i1] == colores[i2]:
            parejas_logradas += 1
        else:
            mostradas[i1] = False
            mostradas[i2] = False
            
        elegidas = []

    if parejas_logradas == 8:
        print("¡Ganaste!")
        jugando = False

pygame.quit()