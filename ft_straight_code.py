def ft_straight_code(a):
    if a >= 0:
        b = a % 2
        while a > 0:
            a = a // 2
            b = b * 10 + a % 2
        print(b)
    if a < 0:
        a = a * - 1
        b = a % 2
        c = 10000000
        while a > 0:
            a = a // 2
            b = b * 10 + a % 2
        print(c + b)
