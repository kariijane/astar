import heapq
import sys

# Функция эвристического рассчёта расстояния
def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# Функция возвращает список координат соседних точек, 
# кроме непроходимых и за границей карты
def get_neighbors(point, map):
    result = []
    x, y = point
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx == 0 and dy == 0):
                continue
            if x + dx < 0 or x + dx >= len(map) or y + dy < 0 or y + dy >= len(map[0]):
                continue
            if map[x + dx][y + dy] :
                continue
            result.append((x + dx, y + dy))
    return result
    
# Функция для поиска пути
def astar(array, start, goal):
    # Создание списка с приоритетной очередью
    open_list = [(0, start)]
    # Создание словаря для хранения стоимости пути до каждой точки
    cost_so_far = {start: 0}
    # Создание словаря для хранения предыдущей точки на пути до каждой точки
    came_from = {start: None}

    while len(open_list) > 0:
        # Извлечение точки с наименьшей стоимостью из приоритетной очереди
        current = heapq.heappop(open_list)[1]

        # Если достигнута целевая точка, то возвращаем путь до нее
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        # Перебор всех соседних точек
        for next in get_neighbors(current, array):
            # Проверка, что соседняя точка находится в пределах матрицы
            if next[0] < 0 or next[0] >= len(array) or next[1] < 0 or next[1] >= len(array[0]):
                continue
            # Проверка, что соседняя точка не является стеной
            if array[next[0]][next[1]] == 1:
                continue
            # Вычисление стоимости пути до соседней точки
            new_cost = cost_so_far[current] + 10
            # Проверка, что новый путь до соседней точки более оптимален, чем предыдущий
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhattan(goal, next)
                heapq.heappush(open_list, (priority, next))
                came_from[next] = current

    # Если целевая точка не достигнута, то возвращаем None
    return None

sys.modules[__name__] = astar