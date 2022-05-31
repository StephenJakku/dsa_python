def lcm(strs):
    print(strs)
    strs.sort(key=len)
    print(strs)
    res=strs[0]
    for str in strs:
        while(res not in str and len(res)>0):
            res=res[:len(res)-1]
    return res

print(lcm(["flower","flow","flight"]))