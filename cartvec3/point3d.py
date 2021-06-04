"""
Module point3d -- 3-element point using double-precision elements.
Includes class Point3d
"""

from cart3d import Cart3d
import math
import array as ar

class Point3d(Cart3d):
    "A 3-element point of double-precision elements."
    prefix = "Point3d."
    #enumx = (0, 1, 2)       # enumeration of indices
    #zeros = [ 0.0, 0.0, 0.0 ]

    def __init__(self, *args) -> None:
        #acnt = len(args)    # argument count
        super().__init__(*args)

    def __repr__(self):
        return Point3d.prefix+self.elems.__repr__()

    def distanceSquared(self, p1):
        "Return square of distance between this point and point p1."
        d2 = 0.0
        for i in Cart3d.enumx:
            d1 = self.elems[i] - p1.elems[i]
            d2 += d1*d1
        return d2

    def distance(self, p1):
        "Return distance between this point and point p1."
        d2 = 0.0
        for i in Cart3d.enumx:
            d1 = self.elems[i] - p1.elems[i]
            d2 += d1*d1
        d = math.sqrt(d2)
        return d



