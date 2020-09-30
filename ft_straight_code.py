def ft_straight_code (a):
    l = 0 
    if a >= 0:
        s = a 
    if a < 0:
        s = a 
        s = s * -1 
    if a % 2 == 0:
        if a >= 0:
            b = a % 2 
            l = 0 
            while a > 0:
                a = a // 2
                b = b * 10 + a % 2 
                l = l + 1 
            m = 8 - l 
            if m == 0:
                l = l * l 
            if m == 1:
                print ("0", end = "") 
            if m == 2:
                print ("00", end = "") 
            if m == 3:
                print ("000", end = "") 
            if m == 4:
                print ("0000", end = "") 
            if m == 5:
                print ("00000", end = "") 
            if m== 6:
                print ("000000", end = "") 
            if m == 7:
                print ("0000000", end = "") 
            if m == 8: 
                print ("0000000", end = "") 
            if s == 4 or s == 8 or s == 16 or s == 32 or s == 64:
                print (b, end = "")
            if s != 4 and s != 8 and s != 16 and s != 32 and s != 64:
                print (b) 
        if a < 0:
            a = a * -1 
            b = a % 2 
            while a > 0:
                a = a // 2
                b = b * 10 + a % 2
                l = l + 1 
            m = 8 - l 
            if m == 0:
                l = l * l 
            if m == 1:
                print ("1", end = "") 
            if m == 2:
                print ("10", end = "") 
            if m == 3:
                print ("100", end = "") 
            if m == 4:
                print ("1000", end = "") 
            if m == 5:
                print ("10000", end = "") 
            if m== 6:
                print ("100000", end = "") 
            if m == 7:
                print ("1000000", end = "") 
            if m == 8: 
                print ("1000000", end = "")
            if s == 4 or s == 8 or s == 16 or s == 32 or s == 64:
                print (b, end = "")
            if s != 4 and s != 8 and s != 16 and s != 32 and s != 64:
                print (b) 
    if a % 2 == 1:
        if a >= 0:
            b = 0 
            l = 0 
            while a > 0:
                b = b * 10 + a % 2
                l = l + 1 
                a = a // 2
            m = 8 - l 
            if m == 1:
                print ("0", end = "") 
            if m == 2:
                print ("00", end = "") 
            if m == 3:
                print ("000", end = "") 
            if m == 4:
                print ("0000", end = "") 
            if m == 5:
                print ("00000", end = "") 
            if m== 6:
                print ("000000", end = "") 
            if m == 7:
                print ("0000000", end = "")
            if m == 8: 
                print ("0000000", end = "")
            print (b) 
        if a < 0:
            a = a * -1 
            b = 0 
            while a > 0:
                b = b * 10 + a % 2 
                a = a // 2
                l = l + 1
            m = 8 - l
            if m == 0:
                l = l * l 
            if m == 1:
                print ("1", end = "") 
            if m == 2:
                print ("10", end = "") 
            if m == 3:
                print ("100", end = "") 
            if m == 4:
                print ("1000", end = "") 
            if m == 5:
                print ("10000", end = "") 
            if m== 6:
                print ("100000", end = "") 
            if m == 7:
                print ("1000000", end = "") 
            if m == 8: 
                print ("1000000", end = "") 
            print (b)
    if s == 4:
        print ("0")
    if s == 8:
        print ("00")
    if s == 16:
        print ("000")
    if s == 32:
        print ("0000")
    if s == 64:
        print ("00000")
