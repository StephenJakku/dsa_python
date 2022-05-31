def addBinary(a: str, b: str) -> str:
    size = len(a) if len(a) > len(b) else len(b)
    # print(size)
    a = a.zfill(size)
    b = b.zfill(size)
    # print(a)
    # print(b)
    res = ""
    carry = 0
    for i in range(size - 1, -1, -1):
        print(f"a[i]: {a[i]} b[i]: {b[i]}")
        if (int(a[i]) == 1 and int(b[i]) == 1):
            if carry == 0:
                res = str(0) + res
                carry = 1
            elif carry == 1:
                res = str(1) + res
        elif int(a[i]) == 0 and int(b[i]) == 0:
            if carry == 0:
                res = str(0) + res
            elif carry == 1:
                res = str(1) + res
                carry=0
        elif (int(a[i]) == 1 and int(b[i]) == 0) or (int(a[i]) == 0 and int(b[i]) == 1):
            if carry == 0:
                res = str(1) + res
            elif carry == 1:
                res = str(0) + res
        print(res)
        print(f"Carry: {carry}")
    # if carry == 1 and (a[0] == 1 and b[0] == 1):
    #     res = '11' + res
    # if carry == 1 and int(res[0]) == 1:
    #     res = '10' + res
    if carry == 1:
        res = '1' + res
    return res

print(addBinary('1111','1111'))