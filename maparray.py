import numpy as np
import random

def generate_normal(array, num):
    # 상하좌우의 값 중 단 하나만 0이 아닌 좌표 찾기
    for _ in range(num):
        non_zero = []
        for x in range(15):
            for y in range(15):
                if array[x][y] == 0 and x != 0 and x != 14 and y != 0 and y != 14:
                    neighbors = [
                        (x-1, y), (x+1, y), (x, y-1), (x, y+1)
                    ]
                    neighbor_check = [array[n[0]][n[1]] for n in neighbors if 0 <= n[0] < 15 and 0 <= n[1] < 15]
                    if neighbor_check.count(0) == 3:
                        non_zero.append((x, y))

        if non_zero:
            # 랜덤하게 좌표 선택하여 1로 변경
            room = random.choice(non_zero)
            array[room[0]][room[1]] = 1

def generate_special(array, n):
    # 상하좌우의 값 중 하나는 1이고 나머지는 0인 좌표 찾기
    non_zero = []
    for x in range(15):
        for y in range(15):
            if array[x][y] == 0 and x != 0 and x != 14 and y != 0 and y != 14:
                neighbors = [
                    (x-1, y), (x+1, y), (x, y-1), (x, y+1)
                ]
                neighbor_check = [array[n[0]][n[1]] for n in neighbors if 0 <= n[0] < 15 and 0 <= n[1] < 15]
                if neighbor_check.count(1) == 1 and neighbor_check.count(0) == 3:
                    non_zero.append((x, y))

    if non_zero:
        # 랜덤하게 좌표 선택하여 a로 변경
        room = random.choice(non_zero)
        array[room[0]][room[1]] = n

def generate_boss(array):
    #중심과 거리가 가장 먼 좌표 찾기
    farthest = (0, 0)
    max_distance = 0
    for x in range(15):
        for y in range(15):
            if array[x][y] == 0 and x != 0 and x != 14 and y != 0 and y != 14:
                neighbors = [
                    (x-1, y), (x+1, y), (x, y-1), (x, y+1)
                ]
                neighbor_check = [array[n[0]][n[1]] for n in neighbors if 0 <= n[0] < 15 and 0 <= n[1] < 15]
                distance = abs(x - 7) + abs(y - 7)
                if neighbor_check.count(1) == 1 and neighbor_check.count(0) == 3 and distance > max_distance:
                    max_distance = distance
                    farthest = (x, y)

    # 랜덤하게 좌표 선택하여 2로 변경
    array[farthest[0]][farthest[1]] = 2

def create_normal(num):
    array = np.zeros((15, 15), dtype=int)
    array[7][7] = 1
    generate_normal(array, num)
    generate_boss(array)
    generate_special(array, 3)
    generate_special(array, 4)
    for x in range(15):
        for y in range(15):
            if x == 0 or x == 14 or y == 0 or y == 14:
                array[x][y] = 9
    return array

# 매개변수 num_iterations과 a에 원하는 값을 전달하여 함수 호출
stage1 = create_normal(8)
stage2 = create_normal(8)
stage3 = create_normal(8)