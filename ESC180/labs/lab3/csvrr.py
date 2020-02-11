f=open('data','r')
lines=f.readlines()
f.close()
accum=[]
for i in lines:
   j=i.split('\n')[0]  # first get rid of the '\n'
   k=j.split(',')      # now split on the comma
   r=[]
   for x in k:
      r = r + [int(x)]
   accum = accum + [r] # accumulate

def sortKey(x):
    return -x[2]
def genSortKey(col, up):
    def key(x):
        if up:
            return x[col]
        else:
            return -x[col]
    return key

sortKey = genSortKey(2,True)

print(sorted(accum, key=sortKey))
