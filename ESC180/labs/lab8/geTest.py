from ge import *

a = [[-1,1],[-1,0],[0,-1],[-1,-2]]
print(ge_fw(a))
print(ge_bw(ge_fw(a)))

a = [[1,3,2,1],[2,-3,0,-2]]
print(ge_fw(a))
print(ge_bw(ge_fw(a)))


a = [[1,2,0],[1,3,3],[-1,0,-1],[-3,0,0]]
print(ge_fw(a))
print(ge_bw(ge_fw(a)))

