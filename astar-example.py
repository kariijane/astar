import pygame as pg
import astar

map = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0],
]

tile = 40
start = (2, 1)
goal = (1, 5)

rows = len(map)
cols = len(map[0])

# вычисление пути
path = astar(map, start, goal)

# возвращает координаты квадрата для pg.draw.rect
def getRect(x, y):
    return x * tile + 1, y * tile + 1, tile - 1, tile - 1

# вывод текста
def drawText(text, cell, offset = [1, 1], color = (255, 255, 255)):
    surface = font.render(text, False, color)
    sc.blit(surface, (cell[0] * tile + offset[0], cell[1] * tile + offset[1]))

# инициализация PyGame для визуализации работы алгоритма
pg.init()
sc = pg.display.set_mode([cols * tile, rows * tile])
clock = pg.time.Clock()
pg.font.init()
font = pg.font.SysFont('Courier New', 12)

# основной цикл работы программы
while True:
    for y, row in enumerate(map): 
        for x, value in enumerate(row):
            # закраска квадратов карты
            if value == 1: 
                pg.draw.rect(sc, pg.Color('darkgray'), getRect(x, y))
            else:
                pg.draw.rect(sc, (40, 24, 14), getRect(x, y))

            # кружочки на пути к цели жёлтые
            if path != None and path.count((y, x)) > 0:
                pg.draw.circle(sc, pg.Color('yellow'), (x * tile + 20, y * tile + 20), 8)

            # координаты квадрата
            drawText(str(y) + "," + str(x), [x, y], [1, 1], (100, 100, 100))
            
            # началная точка с зелёным кружком
            if (y, x) == start:
                pg.draw.circle(sc, pg.Color('green'), (x * tile + 20, y * tile + 20), 5)
            # целевая точка с красным кружком
            if (y, x) == goal:
                pg.draw.circle(sc, pg.Color('red'), (x * tile + 20, y * tile + 20), 5)

    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(30)