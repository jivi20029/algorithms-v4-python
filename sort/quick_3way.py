# 三向切分快速排序主要是加快重复项比较多的情况下的排序速度


def less(v, w):
    return v < w


def exch(a, i, j):
    a[i], a[j] = a[j], a[i]


def show(a):
    for item in a:
        print(item, sep=' ')
    print('')


def isSorted(a):
    for i in range(1, len(a)):
        if less(a[i], a[i-1]):
            return False
    return True


# def partition(a, lo, hi):
#     i = lo
#     j = hi + 1
#     v = a[lo]

#     # print(i, j, v)
#     while True:
#         i += 1
#         while less(a[i], v):
#             if i == hi:
#                 break
#             i += 1

#         j -= 1
#         while less(v, a[j]):
#             if j == lo:
#                 break
#             j -= 1

#         # print(i, j)

#         if i >= j:
#             break

#         exch(a, i, j)

#     exch(a, lo, j)

#     return j


def sort1(a, lo, hi):
    if lo >= hi:
        return

    # j = partition(a, lo, hi)
    # # print(lo, hi, j)
    # # print(a)
    # sort1(a, lo, j-1)
    # sort1(a, j+1, hi)
    lt = lo
    i = lo + 1
    gt = hi
    v = a[lo]
    while i <= gt:
        if a[i] < v:
            exch(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > v:
            exch(a, gt, i)
            gt -= 1
            # i += 1
        else:
            i += 1

    sort1(a, lo, lt-1)
    sort1(a, gt+1, hi)


def sort(a):
    from random import shuffle
    shuffle(a)
    # print(a)
    sort1(a, 0, len(a)-1)


if __name__ == '__main__':
    a = [2, 3, 2, 8, 12, 10, 10, 8, 2, 3, 2, 3, 8, 12, 10]
    # [3, 9, 7, 1, 2, 6]
    sort(a)
    assert isSorted(a)
    show(a)
