def rule(val, ls):
    tot = 0
    for i in ls:
        tot = tot + i
    if val == 1:
        if tot == 2 or tot == 3:
            return 1
        else:
            return 0
    else:
        if tot == 3:
            return 1
        else:
            return 0
