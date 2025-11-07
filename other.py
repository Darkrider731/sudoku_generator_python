import pygame
import random

box_1 = [0, 1, 2]
box_2 = [3, 4, 5]
box_3 = [6, 7, 8]

position = 0

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]


]
for y in grid:
  #for i in y:
    print(y)

def get_val(grid, position):
    while True:
        if position < 9:
            number = 1
            print(1)
        elif 8 < position < 18:
            number = 2
            print(2)
        elif 17 < position < 27:
            number = 3
        elif 26 < position < 36:
            number = 4
        elif 35 < position < 45:
            number = 5
        elif 44 < position < 54:
            number = 6
        elif 53 < position < 63:
            number = 7
        elif 62 < position < 72:
            number = 8
        elif 71 < position < 81:
            number = 9
        else:
            exit(position)
        x_ax = random.randint(0, 8)
        y_ax = random.randint(0, 8)

        if grid[y_ax][x_ax] == 0:
            return x_ax, y_ax, number


def which_box(position_x, position_y):
    global box_1, box_2, box_3
    if -1 < position_x < 3:
        x = box_1
    elif 2 < position_x < 6:
        x = box_2
    elif 5 < position_x < 9:
        x = box_3
    if -1 < position_y < 3:
        y = box_1
    elif 2 < position_y < 6:
        y = box_2
    elif 5 < position_y < 9:
        y = box_3
    return x, y


def if_in_box(choosen_num, position_x, position_y, grid):
    x_box, y_box = which_box(position_x, position_y)
    for y in y_box:
        for x in x_box:
            if choosen_num == grid[y][x]:
                #print(f" {choosen_num} exists in box {x_box} x {y_box} y")
                return True
    return False




def if_in_x(choosen_num, position_x, grid):
    for x_row in grid:
        if choosen_num == x_row[position_x]:
            #print(f" {choosen_num} exists in row {position_x} x {x_row[position_x]}{position_x}{x_row}")
            return True
    return False


def if_in_y(choosen_num, position_y, grid):
    if choosen_num in grid[position_y]:
        #print(f" {choosen_num} exists in row {position_y} y")

        return True
    return False





def add_number_to_grid(grid, position):
    exists = False
    position_x, position_y, choosen_number = get_val(grid, position)
    exists = if_in_x(choosen_number, position_x, grid)
    if exists:

        return grid, position, choosen_number
    exists = if_in_y(choosen_number, position_y, grid)
    if exists:

        return grid, position, choosen_number
    exists = if_in_box(choosen_number, position_x, position_y, grid)
    if exists:

        return grid, position, choosen_number

    grid[position_y][position_x] = choosen_number
    print("            new grid")
    for row in grid:
        print(row)
    position += 1
    return grid, position, choosen_number




def run_script(grid):
    position = 0
    cycle = 0
    oldnumb = 1
    x_cor = 0
    y_cor = 0
    while True:
        grid, position, numb = add_number_to_grid(grid, position)
        if numb != oldnumb:
            cycle = 0
        oldnumb = numb
        cycle += 1
        if cycle > 10000000:
            cycle = 0
            for row in grid:

                for position in row:
                    if position == numb:
                        print(f"{x_cor}x,  y{y_cor}")
                        grid[x_cor][y_cor] = 0
                    y_cor += 1
                y_cor = 0
                x_cor += 1
            x_cor = 0
            y_cor = 0
            """if position < 9:
                position = 0
                print(1)"""
            if 8 < position < 18:
                position = 9
                print(2)
            elif 17 < position < 27:
                position = 18
            elif 26 < position < 36:
                position = 27
            elif 35 < position < 45:
                position = 36
            elif 44 < position < 54:
                position = 45
            elif 53 < position < 63:
                position = 54
            elif 62 < position < 72:
                position = 63
            elif 71 < position < 81:
                position = 72


run_script(grid)
