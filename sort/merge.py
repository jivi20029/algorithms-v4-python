def less(v, w):
    return v < w


def exch(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def show(a):
    for item in a:
        print(item, sep=' ')
    print('')


def isSorted(a):
    for i in range(1, len(a)):
        if less(a[i], a[i-1]):
            return False
    return True


aux = []


def merge(a, lo, mid, hi):
    # print(lo, mid, hi)
    global aux
    i = lo
    j = mid + 1

    for k in range(lo, hi+1):
        aux[k] = a[k]

    # print(aux)

    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif less(aux[j], aux[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


def sort1(a, lo, hi):
    if hi <= lo:
        return
    mid = lo + int((hi-lo)/2)
    sort1(a, lo, mid)
    sort1(a, mid+1, hi)
    merge(a, lo, mid, hi)


def sort(a):
    global aux
    aux = list(range(len(a)))
    sort1(a, 0, len(a)-1)


if __name__ == '__main__':
    a = [2, 6, 7, 3, 1, 9, 10, 12]
    sort(a)
    assert isSorted(a)
    show(a)
