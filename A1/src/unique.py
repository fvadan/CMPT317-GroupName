import copy

"""
    UniqueHashable class implementation. UniqueHashable implemented due to
    requirements of uniqueness of states in Python dictionaries. Particular
    classes can be made unique hashable by hashing the arguments, keyword
    arguments, and class itself.

    Authors: Mahmud Ahzam*, Tayab Soomro*, Flaviu Vadan*
    Class: CMPT317
    Instructor: Michael Horsch
    Assignment: 1

    * - all authors equally contributed to the implementation 
"""

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
