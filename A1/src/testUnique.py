from problemState import Vehicle, Package, State
from dataStructures import HashableDictionary

"""
    TestUnique file that tests whether classes instantiated with the same
    parameters will hash to the same locations. Testing based on unique
    hashable.

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation 
"""

v1 = Vehicle((0,), 0, 2)
v1_copy = Vehicle((0,), 0, 2)

v3 = Vehicle((0,), 1, 2)
v3_copy = Vehicle((0,), 1, 2)

v4 = Vehicle((0,), 2, 2)
v4_copy = Vehicle((0,), 2, 2)

p1 = Package((2,), (3,), 0, False)
p1_copy = Package((2,), (3,), 0, False)

p3 = Package((3,), (4,), 1, False)
p3_copy = Package((3,), (4,), 1, False)

p4 = Package((6,), (5,), 2, False)
p4_copy = Package((6,), (5,), 2, False)

p5 = Package((5,), (4,), 3, False)
p5_copy = Package((5,), (4,), 3, False)

p6 = Package((4,), (3,), 4, False)
p6_copy = Package((4,), (3,), 4, False)

lv = [v1,v3,v4]
lv_copy = [v1_copy, v3_copy, v4_copy]

l = [p1,p3,p4,p5,p6]
l_copy = [p1_copy,p3_copy,p4_copy,p5_copy,p6_copy]

assert([1,2,3] == [1,2,3])
assert(l == l_copy)

packages = {}
packages_hash = HashableDictionary("PACKAGES")
packages_hash_copy = HashableDictionary("PACKAGES")

vehicles = {}
vehicles_hash = HashableDictionary("VEHICLES")
vehicles_hash_copy = HashableDictionary("VEHICLES")

packages[p1] = True
packages[p3] = True
packages[p4] = False
packages[p5] = False
packages[p6] = True

vehicles[v1] = True
vehicles[v3] = False
vehicles[v4] = True

for i in range(len(l_copy)):
    assert(packages[l[i]] == packages[l_copy[i]])
    assert(l[i] == l_copy[i])
    packages_hash[l[i].getIndex()] = l[i]
    packages_hash_copy[l[i].getIndex()] = l_copy[i]
    assert(hash(packages_hash) == hash(packages_hash_copy))

for i in range(len(lv_copy)):
    assert(vehicles[lv[i]] == vehicles[lv_copy[i]])
    assert(lv[i] == lv_copy[i])
    vehicles_hash[lv[i].getIndex()] = lv[i]
    vehicles_hash_copy[lv[i].getIndex()] = lv_copy[i]
    assert(hash(vehicles_hash) == hash(vehicles_hash_copy))

st = State(vehicles_hash, packages_hash)
st_copy = State(vehicles_hash_copy, packages_hash_copy)

print(st)
print(st_copy)
assert(hash(st.getVehicles()) == hash(st_copy.getVehicles()))
assert(hash(st.getPackages()) == hash(st_copy.getPackages()))
assert(hash(st) == hash(st_copy))
assert(st == st_copy)

states = {}

states[st] = True
states[st_copy] = False

states_hash = HashableDictionary("States")
states_hash[st] = True
states_hash[st_copy] = False

for k,v in states.items():
    print(k)
    print(v)

assert(len(states) == 1)
assert(states[st] == False)
assert(len(states_hash) == 1)
assert(states_hash[st] == False)
