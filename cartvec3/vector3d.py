"""
Module vector3d -- 3-element vector using double-precision elements.
Includes class Vector3d
"""

from cart3d import Cart3d
import array as ar
import math

def _lenSq(v):
    "length squared of a vector."
    s = 0.0
    for i in Cart3d.enumx:
        s += v.elems[i] * v.elems[i]
    return s

def normalize(v):
    "Normalize a vector to unit length."
    lsq = _lenSq(v)
    norm = 1.0 / math.sqrt(lsq)
    v1 = v * norm
    return v1

class Vector3d(Cart3d):
    "A 3-element vector of double-precision elements."
    prefix = "Vector3d."
    #enumx = (0, 1, 2)       # enumeration of indices
    #zeros = [ 0.0, 0.0, 0.0 ]

    def __init__(self, *args) -> None:
        #acnt = len(args)    # argument count
        super().__init__(*args)

    def __repr__(self):
        return Vector3d.prefix+self.elems.__repr__()

    def __matmul__(self, v2):
        # Vector3d @ Vector3d (cross product)
        v0 = Vector3d()
        v1 = self
        v0.elems[0] = v1.elems[1]*v2.elems[2] - v1.elems[2]*v2.elems[1]
        v0.elems[1] = v1.elems[2]*v2.elems[0] - v1.elems[0]*v2.elems[2]
        v0.elems[2] = v1.elems[0]*v2.elems[1] - v1.elems[1]*v2.elems[0]
        return v0

    def normalize(self):
        "Normalize vector in-place. No return value."
        lsq = _lenSq(self)
        norm = 1.0 / math.sqrt(lsq)
        for i in Cart3d.enumx:
            self.elems[i] *= norm

    def lengthSquared(self):
        "Return the squared length of this vector."
        return _lenSq(self)

    def length(self):
        "Return the length of this vector."
        return math.sqrt(_lenSq(self))

    def angle(self, v1):
        "Return the angle in radians between self and argument vectors."
        cosa = (self * v1) / (self.length() * v1.length())
        return math.acos(cosa)

