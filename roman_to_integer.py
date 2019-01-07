def romant_to_integer(roman : str):
    total = 0
    a = list(s)
    for i in range(0, len(a)):
        if i + 1 < len(a):
            if a[i] == 'I' and a[i+1] == 'V':
                total += 4
                a[i+1] = 0
            elif a[i] == 'I' and a[i+1] == 'X':
                total += 9
                a[i+1] = 0
            elif a[i] == 'X' and a[i+1] == 'L':
                total += 40
                a[i+1] = 0
            elif a[i] == 'X' and a[i+1] == 'C':
                total += 90
                a[i+1] = 0
            elif a[i] == 'C' and a[i+1] == 'D':
                total += 400
                a[i+1] = 0
            elif a[i] == 'C' and a[i+1] == 'M':
                total += 900
                a [i+1] = 0
            elif a[i] == 'I':
                total += 1
            elif a[i] == 'V':
                total += 5
            elif a[i] == 'X':
                total += 10
            elif a[i] == 'L':
                total+= 50
            elif a[i] == 'C':
                total += 100
            elif a[i] == 'D':
                total += 500
            elif a[i] == 'M':
                total += 1000
        else:
            if a[i] == 'I':
                total += 1
            elif a[i] == 'V':
                total += 5
            elif a[i] == 'X':
                total += 10
            elif a[i] == 'L':
                total+= 50
            elif a[i] == 'C':
                total += 100
            elif a[i] == 'D':
                total += 500
            elif a[i] == 'M':
                total += 1000
    return total