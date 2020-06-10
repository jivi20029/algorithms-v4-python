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
    h = 1
    while h < N/3:
        h = 3*h + 1
        # print(h)

    # print('---')
    while h >= 1:
        for i in range(h, N):
            # print(i, h-1, -1*h)
            for j in range(i, h-1, -1*h):
                if less(a[j], a[j-h]):
                    exch(a, j, j-h)
                else:
                    break

        h = int(h/3)
        # print(h, '---')


if __name__ == '__main__':
    a = [2, 6, 7, 3, 1, 9, 10, 12, 1, 21, 26, 22, 10]
    sort(a)
    assert isSorted(a)
    show(a)
