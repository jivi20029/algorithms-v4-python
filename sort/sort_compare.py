import time
import random
import importlib
import sys


def time1(alg, a):
    begin_time = time.time()
    sort_module = importlib.import_module(alg)
    sort = getattr(sort_module, 'sort')
    sort(a)
    end_time = time.time()
    return end_time - begin_time


def time_random_input(alg, N, T):
    total = 0
    for _ in range(T):
        a = [round(random.random()*N, 2) for _ in range(N)]
        # 有序状态下 插入比选择快得多
        # a = [i for i in range(N)]
        total += time1(alg, a)

    return total


args = sys.argv[1:]
alg1 = args[0]
alg2 = args[1]

N = int(args[2])
T = int(args[3])

# print(alg1, alg2, N, T)
t1 = time_random_input(alg1, N, T)
t2 = time_random_input(alg2, N, T)

print(f"For {N} random float\n {alg1} is {round(t2/t1,1)} times faster than {alg2}")
