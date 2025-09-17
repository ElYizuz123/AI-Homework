import pygame

# Configuraciones iniciales
ANCHO_VENTANA = 800
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ANCHO_VENTANA))
pygame.display.set_caption("Visualización de Nodos")

# Colores (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
GRIS_BAJO = (169, 169, 169)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NARANJA = (255, 165, 0)
PURPURA = (128, 0, 128)

class Nodo:
    def __init__(self, fila, col, ancho, total_filas):
        self.fila = fila
        self.col = col
        self.x = fila * ancho
        self.y = col * ancho
        self.color = BLANCO
        self.ancho = ancho
        self.total_filas = total_filas

    def get_pos(self):
        return self.fila, self.col

    def es_pared(self):
        return self.color == NEGRO

    def es_inicio(self):
        return self.color == NARANJA

    def es_fin(self):
        return self.color == PURPURA

    def restablecer(self):
        self.color = BLANCO

    def hacer_inicio(self):
        self.color = NARANJA

    def hacer_pared(self):
        self.color = NEGRO

    def hacer_fin(self):
        self.color = PURPURA
    
    def hacer_la(self):
        self.color = GRIS_BAJO
        
    def hacer_lc(self):
        self.color = AZUL

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, (self.x, self.y, self.ancho, self.ancho))

class NodoAStar(Nodo):
    def __init__(self, fila, col, ancho, total_filas, padre=None, distancia=None, h=None):
        super().__init__(fila, col, ancho, total_filas)
        if distancia is not None and h is not None:
            self.distancia = distancia
            self.h = h
            self.total = distancia + h
            self.padre = padre
        else:
            self.distancia = float("inf")
            self.h = float("inf")
            self.total = float("inf")
            self.padre = None
        self.vecinos = []

    # Vecinos
    def actualizar_vecinos(self, grid):
        self.vecinos = []
        # Abajo
        if self.fila < self.total_filas - 1 and not grid[self.fila + 1][self.col].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila + 1][self.col].fila, 
                                          grid[self.fila + 1][self.col].col, 
                                          self.ancho, self.total_filas, 
                                          self, 
                                          self.distancia + 10, 
                                          0))
        # Arriba
        if self.fila > 0 and not grid[self.fila - 1][self.col].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila - 1][self.col].fila, 
                                          grid[self.fila - 1][self.col].col, 
                                          self.ancho, self.total_filas, self, 
                                          self.distancia + 10, 
                                          0))
        # Derecha
        if self.col < self.total_filas - 1 and not grid[self.fila][self.col + 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila][self.col + 1].fila, 
                                          grid[self.fila][self.col + 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 10, 
                                          0))
        # Izquierda
        if self.col > 0 and not grid[self.fila][self.col - 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila][self.col - 1].fila, 
                                          grid[self.fila][self.col - 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 10, 
                                          0))
        # Diagonal abajo-derecha
        if self.fila < self.total_filas - 1 and self.col < self.total_filas - 1 and not grid[self.fila + 1][self.col + 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila + 1][self.col + 1].fila, 
                                          grid[self.fila + 1][self.col + 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 15, 
                                          0))
        # Diagonal abajo-izquierda
        if self.fila < self.total_filas - 1 and self.col > 0 and not grid[self.fila + 1][self.col - 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila + 1][self.col - 1].fila, 
                                          grid[self.fila + 1][self.col - 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 15, 
                                          0))
        # Diagonal arriba-derecha
        if self.fila > 0 and self.col < self.total_filas - 1 and not grid[self.fila - 1][self.col + 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila - 1][self.col + 1].fila, 
                                          grid[self.fila - 1][self.col + 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 15, 
                                          0))
        # Diagonal arriba-izquierda
        if self.fila > 0 and self.col > 0 and not grid[self.fila - 1][self.col - 1].es_pared():
            self.vecinos.append(NodoAStar(grid[self.fila - 1][self.col - 1].fila, 
                                          grid[self.fila - 1][self.col - 1].col, 
                                          self.ancho, 
                                          self.total_filas, 
                                          self, 
                                          self.distancia + 15, 
                                          0))

def crear_grid(filas, ancho):
    grid = []
    ancho_nodo = ancho // filas
    for i in range(filas):
        grid.append([])
        for j in range(filas):
            nodo = Nodo(i, j, ancho_nodo, filas)
            grid[i].append(nodo)
    return grid

def dibujar_grid(ventana, filas, ancho):
    ancho_nodo = ancho // filas
    for i in range(filas):
        pygame.draw.line(ventana, GRIS, (0, i * ancho_nodo), (ancho, i * ancho_nodo))
        for j in range(filas):
            pygame.draw.line(ventana, GRIS, (j * ancho_nodo, 0), (j * ancho_nodo, ancho))

def dibujar(ventana, grid, filas, ancho):
    ventana.fill(BLANCO)
    for fila in grid:
        for nodo in fila:
            nodo.dibujar(ventana)

    dibujar_grid(ventana, filas, ancho)
    pygame.display.update()

def obtener_click_pos(pos, filas, ancho):
    ancho_nodo = ancho // filas
    y, x = pos
    fila = y // ancho_nodo
    col = x // ancho_nodo
    return fila, col

def algoritmo_aStar(fin, lc, la, grid, actual):
    i = 0
    while(i < 2):
        actual.actualizar_vecinos(grid)
        for vecino in actual.vecinos:
            if la[vecino.fila][vecino.col] is None and lc[vecino.fila][vecino.col] is None:
                la[vecino.fila][vecino.col] = vecino
                grid[vecino.fila][vecino.col].hacer_la()
                print(f"Agregando a LA: ({vecino.fila}, {vecino.col}) con total {vecino.total}")
            elif la[vecino.fila][vecino.col] is not None and vecino.total < la[vecino.fila][vecino.col].total:
                la[vecino.fila][vecino.col] = vecino
        nodos_la = [nodo for fila in la for nodo in fila if nodo is not None]
        actual = min(nodos_la, key=lambda x: x.total) if nodos_la else None
        print(f"Actual: ({actual.fila}, {actual.col}) con total {actual.total}" if actual else "No hay nodos en LA")
        if actual is None:
            print("No hay camino posible")
            return
        lc[actual.fila][actual.col] = actual
        la[actual.fila][actual.col] = None
        grid[actual.fila][actual.col].hacer_lc()

        i += 1

def actualizarLA(la, actual, grid):
    pass

def main(ventana, ancho):
    FILAS = 10
    grid = crear_grid(FILAS, ancho)

    inicio = None
    fin = None

    corriendo = True

    while corriendo:
        dibujar(ventana, grid, FILAS, ancho)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if pygame.mouse.get_pressed()[0]:  # Click izquierdo
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                if not inicio and nodo != fin:
                    inicio = nodo
                    inicio.hacer_inicio()

                elif not fin and nodo != inicio:
                    fin = nodo
                    fin.hacer_fin()

                elif nodo != fin and nodo != inicio:
                    nodo.hacer_pared()

            elif pygame.mouse.get_pressed()[2]:  # Click derecho
                pos = pygame.mouse.get_pos()
                fila, col = obtener_click_pos(pos, FILAS, ancho)
                nodo = grid[fila][col]
                nodo.restablecer()
                if nodo == inicio:
                    inicio = None
                elif nodo == fin:
                    fin = None

            elif pygame.key.get_pressed()[pygame.K_RETURN]:  # Tecla 'enter' para empezar
                if(inicio and fin):
                    print("TODO: Implementar algoritmo A* aquí")
                    actual = NodoAStar(inicio.fila, inicio.col, inicio.ancho, inicio.total_filas, None, 0, 0)
                    lc = [[None for _ in range(FILAS)] for _ in range(FILAS)]
                    la = [[None for _ in range(FILAS)] for _ in range(FILAS)]
                    lc[actual.fila][actual.col] = actual
                    algoritmo_aStar(fin, lc, la, grid, actual)
                else:
                    print("Por favor, selecciona un nodo de inicio y fin.")
                

    pygame.quit()

main(VENTANA, ANCHO_VENTANA)