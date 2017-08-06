# python 3.5.2


def get_fibonacci_by_index(index):
    if index in [1, 2]:
        return 1

    fibs = [1, 1]

    for i in range(3, index + 1):
        c = fibs[i-2] + fibs[i-3]
        fibs.append(c)

    return fibs[-1]
