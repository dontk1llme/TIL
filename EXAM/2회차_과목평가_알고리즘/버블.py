a = [55, 7, 78, 12, 42]
N = len(a)


def bubble_sort(a, N):
    for i in range(N - 1, 0, -1):
        for j in range(1, i + 1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


print(bubble_sort(a, N))
