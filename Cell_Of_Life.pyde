
def check_neighbour(arr, a, b):
    next_gen = [0 for i in range(a*b)]
    for l in range(1, a - 1):
        for m in range(1, b - 1):
            alive = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    alive += arr[(l+i) + (m+j) * cols]
            alive -= arr[l + m * cols]
            
            if arr[l + m * cols] == 1 and alive < 2:
                next_gen[l + m * cols] = 0
            elif arr[l + m * cols] == 1 and alive > 3:
                next_gen[l + m * cols] = 0
            elif arr[l + m * cols] == 1 and alive == 3:
                next_gen[l + m * cols] = 1
            else:
                next_gen[l + m * cols] = arr[l + m * cols]

    return next_gen



def setup():
    global rows, cols, cell, w, cells
    size(600, 600)
    w = 30
    cols = width/w
    rows = height/w
    cells = [0 for i in range(rows*cols)]
    for i in range(cols * 5):
        index = int(random(rows*cols))
        cells[index] = 1


def draw():
    background(0)

    for i in range(len(cells)):
        if cells[i] == 1:
            y = int(i/cols)
            x = i - y * cols
            fill(0, 0, 255)
            rect(x*w, y*w, w, w)
        
    value = check_neighbour(cells, rows, cols)
    
    if mousePressed:
        for v in range(len(value)):
            if value[v] == 1:
                y = int(v/cols)
                x = v - y * cols
                fill(0, 255, 0)
                rect(x*w, y*w, w, w)
        noLoop()
