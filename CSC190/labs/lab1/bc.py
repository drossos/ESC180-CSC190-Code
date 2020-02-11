from stackLib import *

def bc():
    inpt = input()
    stck = Stack()
    count = 0
    for i in inpt:
        if (i == "[" or i == "(" or i == "{"):
            stck.push(i)    
        
        if (i == "]" or i == ")" or i == "}"):
            temp = stck.pop()
            if (i == "]" and temp != "[" or i == ")" and temp != "("  or i == "}" and temp != "{"):
                return [False,count]
        count = count + 1

    if (stck.ls == []):
        return [True,0]
    else:
        return [False,count]   


print(bc()) 
