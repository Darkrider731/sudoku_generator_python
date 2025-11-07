import random
import sys
import time


def create_grid():
    grid = []
    for num in range(9):
        grid.append([])

    for item in grid:
        for i in range(9):
            item.append(0)
    return grid

#grid = create_grid()

'''for line in grid:
    print(line)'''


def which_box(pos_line, pos_num):
    box_1, box_2, box_3 = [0, 1, 2], [3, 4, 5], [6, 7, 8]
    if -1 < pos_line < 3:
        pos_line = box_1
    elif 2 < pos_line < 6:
        pos_line = box_2
    elif 5 < pos_line < 9:
        pos_line = box_3
    if -1 < pos_num < 3:
        pos_num = box_1
    elif 2 < pos_num < 6:
        pos_num = box_2
    elif 5 < pos_num < 9:
        pos_num = box_3
    return pos_line, pos_num


def if_allowed(grid, choosen_num, pos_line, pos_num):
    if choosen_num in grid[pos_line]:
        return False
    for row in grid:
        if choosen_num == row[pos_num]:
            return False
    pos_line, pos_num = which_box(pos_line, pos_num)
    for y in pos_line:
        for x in pos_num:
            if choosen_num == grid[y][x]:
                return False
    return True

def fill_row(pos_line, grid):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    avail_space =[0, 1, 2, 3, 4, 5, 6, 7, 8]
    while len(numbers) > 0:
        allowed = False
        tried = False
        index_num = random.randrange(len(numbers))
        index_space = random.randrange(len(avail_space))
        choosen_number = numbers[index_num]
        pos_num = avail_space[index_space]
        temp_list = []


        for item in avail_space:
            temp_list.append(item)
        while not allowed:
            if tried:
                temp_list.remove(pos_num)
                if len(temp_list) == 0:
                    return grid, pos_line

                index_space = random.randrange(len(temp_list))
                pos_num = temp_list[index_space]
            allowed = if_allowed(grid, choosen_number, pos_line, pos_num)
            if not allowed:
                tried = True
        grid[pos_line][pos_num] = choosen_number

        numbers.remove(choosen_number)
        avail_space.remove(pos_num)
    pos_line += 1
    return grid, pos_line


def check_full(grid):
    for row in grid:
        for num in row:
            if num == 0:
                return False
    return True

def test():
    grid = create_grid()
    pos_line = 0
    full = False
    loop = 0
    attempts = 0
    while not full:
        while loop < 1000:#00:
            if full:
                print(f"took {attempts} attempts   loop {loop} ")
                return grid
            grid, pos_line = fill_row(pos_line, grid)
            '''
            print("new grid")
            for line in grid:
                print(line)'''
            full = check_full(grid)
            loop += 1
            #print(loop)
        loop = 0
        attempts +=1
        #print(f"TRIAL {attempts} loop {loop} ")
        #sys.stdout.write("\033[k")#\033[1G)
        '''for line in grid:
            print(line)'''
        grid = create_grid()
        pos_line = 0
    return grid

time_list = []

while __name__ == '__main__':
    start = time.time()
    print("loading...")
    grid = test()
    end = time.time()
    time_taken = end - start
    print(f"success\ntook {time_taken} seconds")
    for line in grid:
        print(line)
    time_list.append(time_taken)
    print(len(time_list))
    if len(time_list) > 50:
        time_list.sort()
        print(time_list)
        exit(12)
#exit(time_taken)
