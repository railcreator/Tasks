import random
from queue import PriorityQueue
def generate_map(m, n, land_ratio=0.3):
    map_ = [[0 for _ in range(n)] for _ in range(m)]

    land_cells = int(m * n * land_ratio)
    while land_cells > 0:
        x, y = random.randint(0, m - 1), random.randint(0, n - 1)
        if map_[x][y] == 0:
            map_[x][y] = 1
            land_cells -= 1

    return map_
def step(point, m, n):
    x, y = point
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n:
            yield nx, ny


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(map_, start, end):
    m, n = len(map_), len(map_[0])

    closed_set = set()
    open_set = {start}

    came_from = {}

    g_score = {point: float('inf') for row in map_ for point in row}
    g_score[start] = 0

    f_score = {point: float('inf') for row in map_ for point in row}
    f_score[start] = heuristic(start, end)

    while open_set:
        current = min(open_set, key=lambda point: f_score[point])

        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in step(current, m, n):
            if map_[neighbor[0]][neighbor[1]] == 1 or neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + 1

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            came_from[neighbor] = current
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)

    return None

def get_input(prompt):
    while True:
        try:
            values = tuple(map(int, input(prompt).split()))
            if len(values) != 2:
                raise ValueError("Введите два числа через пробел")
            if (values[0] < 1 or values[1] < 1):
                raise ValueError("Введите только положительные числа")
            return values
        except ValueError as e:
            print(f"Ошибка: {e}. Повторите ввод.")
def main():
    m, n = get_input("Введите M и N: ")
    a = get_input("Введите координаты точки A (x, y): ")
    b = get_input("Введите координаты точки B (x, y): ")

    map_ = generate_map(m, n)

    for row in map_:
        print(''.join('O' if cell == 1 else '.' for cell in row))

    path = a_star(map_, a, b)

    if path:
        print("Кратчайший путь: ", path)
    else:
        print("Путь не найден.")


if __name__ == "__main__":
    main()
