def mySqrt(x: int) -> int:
    y = 1

    while y * y <= x // 2:
        y += 1

    return y - 1

print(mySqrt(4))