from random import sample

def more_then(num):
    list = sample(range(num * 3), num)
    print(list)
    return [list[num] for num in range(1, len(list)) if list[num] > list[num - 1]]

print(more_then(int(input())))