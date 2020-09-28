def ft_reverse_code(a):
    if a < 0:
        a = a * -1
        b = a % 2
        while a > 0:
            a = a // 2
            b = b * 10 + a % 2
            m = 11111111
        print(m-b)
