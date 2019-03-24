#### Reference - https://www.i-programmer.info/babbages-bag/291-the-meaning-of-life.html


def setup():
    global rows, cols, cell, w, cells
    size(1000, 1000)
    w = 20
    cols = int(width/w)
    rows = int(height/w)
    cells = [0 for i in range(cols*rows)]
    n = 10       # Length of line of cells
    activate_cells(n)
    
def draw():
    global cells
    background(0)
    frameRate(1)

    for i in range(len(cells)):
        if cells[i] == 1:
            y = int(i/cols)
            x = int(i - y * cols)
            fill(0, 0, 255)
            rect(x*w, y*w, w, w)
                
    value = check_neighbour(cells, cols, rows)
    cells = value[:]
    
    
def check_neighbour(arr, a, b):
    next_gen = [0 for i in range(a*b)]
    for l in range(a):
        for m in range(b):        
            alive = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (m + j) + (l + i) * cols < rows*cols:
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
    start_index = int(rows*cols / 2 + rows / 2 - n / 2)
    for i in range(start_index, start_index + n):
        cells[i] = 1



    
