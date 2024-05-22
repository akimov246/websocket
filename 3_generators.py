from time import time


def gen(s: str):
    for i in s:
        yield i

def gen_filename():
    while True:
        t = int(time() * 1000)
        pattern = f'file-{t}.jpeg'
        yield pattern

        print(2+ 2)

def gen2(n):
    for i in range(n):
        yield i

g1 = gen('leo')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i, end='')
        tasks.append(task)
    except StopIteration:
        pass


