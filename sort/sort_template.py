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
    return None


if __name__ == '__main__':
    a = [2, 6, 7, 3, 1, 9]
    sort(a)
    assert isSorted(a)
    show(a)
