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


def sort(a):
    N = len(a)
    for i in range(0, N):
        min = i
        for j in range(i+1, N):
            if less(a[j], a[min]):
                min = j
        exch(a, i, min)


if __name__ == '__main__':
    # par = input('')
    # a = par.split(' ')
    a = [2, 6, 7, 3, 1, 9]
    # count = 100
    # a = [random.randint(0, count*6) for _ in range(count)]
    sort(a)
    assert isSorted(a)
    show(a)
