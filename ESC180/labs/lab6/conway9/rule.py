def rule(val, ls):
    sum = 0
    for i in ls:
        sum += i
    
    if (val == 1):
       if sum ==2 or sum==3:
            return 1
    else:
        return 0


