import tree
from binary_tree import *

a=binary_tree(1)
b=binary_tree(2)
c=binary_tree(3)
d = binary_tree(4)
e = binary_tree(5)
a.AddLeft(b)
b.AddLeft(e)
b.AddRight(c)
c.AddRight(d)
print(a.Get_LevelOrder())

temp = a.ConvertToTree()[1]
print(temp.Get_LevelOrder())


a=tree.tree(1)
b=tree.tree(2)
c=tree.tree(3)
d = tree.tree(4)
e = tree.tree(5)
a.AddSuccessor(b)
a.AddSuccessor(c)
a.AddSuccessor(d)
b.AddSuccessor(e)

tempS = a.Get_LevelOrder()
print(tempS)

z = a.ConvertToBinaryTree()
print(z.Get_LevelOrder())

"""
x=binary_tree(1)
x.AddLeft(binary_tree(2))
y=binary_tree(3)
y.AddLeft(binary_tree(4))
y.AddRight(binary_tree(5))
x.AddRight(y)
print(x.Get_LevelOrder())
"""

