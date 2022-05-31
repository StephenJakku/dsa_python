def process(p,m):
    max=0
    for i in range(len(p)-m+1):
        print(f"max: {max}, sum{p[i:m+i]}")
        if max<sum(p[i:m+i]):
            max=sum(p[i:m+i])
    print(max)
    return sum(p)-max

p=[10,4,8,13,20]
m=3
print(sum(p))
print(process(p,m))