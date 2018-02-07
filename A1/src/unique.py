
import copy

UNIQUE_INSTANCES = {}

class UniqueHashable:
    def __new__(cls, *args, **kwargs):
        if (args,cls) in UNIQUE_INSTANCES:
            return UNIQUE_INSTANCES[(args,cls)]
        else:
            inst = super(UniqueHashable, cls).__new__(cls)
            inst.__init__(*args, **kwargs)
            UNIQUE_INSTANCES[(args,cls)] = inst
            return inst

class Ab(UniqueHashable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __hash__(self):
        return hash((self.a, self.b))

"""
obj = Ab(5,6)
obj2 = Ab(5,6)
assert obj is obj2
table = {}
table[obj] = 1
table[obj2] = 2
l1 = [Ab(1,i) for i in range(10)]
l2 = [Ab(1,i) for i in range(10)]
assert(hash(tuple(l1)) == hash(tuple(l2)))
assert(obj == obj2)
assert(2 == table[obj])
"""

