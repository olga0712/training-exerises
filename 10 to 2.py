def persistence(n):
    j = 0
    while True:
        temp = 1
        for i in str(n):
            temp *= int(i)
        n = temp
        j += 1
        print(n)
        if n < 10:
            break
    return(j)



persistence(111)
