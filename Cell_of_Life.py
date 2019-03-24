import pygame as py


def check_neighbour(arr, a, b):
    next_gen = [0 for _ in range(a * b)]
    for l in range(a):
        for m in range(b):
            alive = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (m + j) + (l + i) * cols < rows * cols:
                        alive += arr[(m + j) + (l + i) * cols]
            alive -= arr[m + l * cols]

            if arr[m + l * cols] == 1 and alive < 2:
                next_gen[m + l * cols] = 0
            elif arr[m + l * cols] == 1 and alive > 3:
                next_gen[m + l * cols] = 0
            elif arr[m + l * cols] == 0 and alive == 3:
                next_gen[m + l * cols] = 1
            else:
                next_gen[m + l * cols] = arr[m + l * cols]

    return next_gen


def activate_cells(n):
    start_index = int(rows * cols / 2 + rows / 2 - n / 2)
    for i in range(start_index, start_index + n):
        cells[i] = 1


py.init()

clock = py.time.Clock()

width, height = 800, 800
screen = py.display.set_mode((width, height))


w = 30
cols = int(width / w)
rows = int(height / w)
cells = [0 for _ in range(cols * rows)]
n = 8                               # Length of line of cells
activate_cells(n)

while True:
    clock.tick(1)
    screen.fill((50, 50, 50))

    for i in range(len(cells)):
        if cells[i] == 1:
            y = int(i / cols)
            x = int(i - y * cols)
            py.draw.rect(screen, (0, 255, 0), [x * w, y * w, w, w], 3)
    value = check_neighbour(cells, cols, rows)
    py.display.update()
    cells = value[:]

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()

