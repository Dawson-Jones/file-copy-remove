def convert_left(x, y, h, w):
    x, y = y, -x
    y = y + h
    return x, y


def convert_right(x, y, h, w):
    x, y = -y, x
    x = x + w
    return x, y


if __name__ == '__main__':
    # print(convert_left(609, 10, 735, 171))
    print(convert_right(643, 12, 727, 179))
    print(convert_right(717, 179, 727, 179))
