from problemState import Vehicle, Package

v1 = Vehicle((0,), 0, 2)
v2 = Vehicle((0,), 0, 2)
v3 = Vehicle((0,), 1, 2)
p1 = Package((2,), (3,), 0, False)
p2 = Package((2,), (3,), 0, False)
assert(v1 == v2)
assert(v3 != v1)
assert(p1 == p2)




