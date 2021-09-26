# RECURSIVE
tree = {
    "one": 1,
    "asdf":"abc"
}

def countem(node, target):
    if node==target:
        return 1
    if isinstance(node,list):
        return sum(countem(subnode, target) for subnode in node)
    if isinstance(node, dict):
        return sum(countem(subnode, target) for subnode in node)
    return 0

countem('blue', 'blue')
countem(['blue','blue','red','red','blue','BLUE'], 'blue')




def path_to(target, node):
    if target == node:
        return f"-> {target!r}"
    elif isinstance (node,list):
        for i, subnode in enumerate(node):
            path = path_to(target, subnode)
            if path:
                return f"[{i}]{path}"
    elif isinstance(node, dict):
        for key, subnode in node.items():
            path = path_to(target, subnode)
            if path:
                return f"[{key!r}]{path}"
    return 'Not found'

print(path_to('abc', 'abc'))
print(path_to('abc',['asdf','asg','abc','asfg','afgs']))
print(path_to('abc', ['bs',['abc','abc','qasdg'],'adsfg','sdfg','abc']))
print(path_to('abc', tree))
print(path_to(7, 'abc'))



# UNIFORM DISTRIBUTION OF NUMBERS 
from random import *
uniform(50,259)

list(range(10,100,5))
randrange(10,100,5)