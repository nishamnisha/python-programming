def pow(x, y):

    powered = x

    if y == 0:
        return 1

    while y > 1:
        powered *= x

        y -= 1

    return powered

