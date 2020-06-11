# imporve but more slower
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


def merge(a, lo, mid, hi):
    # print(lo, mid, hi)
    i = lo
    j = mid + 1
    aux = list(range(len(a)))

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
    # use the insert sort if count < 15
    # but more slower
    # maybe some wrong
    if hi-lo < 15:
        # print(lo, hi, len(a))
        for i in range(lo+1, hi+1):
            for j in range(i, lo, -1):
                # print(i, j)
                if less(a[j], a[j-1]):
                    exch(a, j, j-1)
                else:
                    break
        # print(a)
        return

    mid = lo + int((hi-lo)/2)
    sort1(a, lo, mid)
    sort1(a, mid+1, hi)
    merge(a, lo, mid, hi)


def sort(a):
    sort1(a, 0, len(a)-1)


if __name__ == '__main__':
    a = [2, 6, 7, 3, 1, 9, 10, 12]
    sort(a)
    assert isSorted(a)
    show(a)
