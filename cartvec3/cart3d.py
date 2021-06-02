"""
Module cart3d -- Cartesian coordinates, 3 axes, double-precision.
Includes class Cart3d.
"""

import array as ar

class Cart3d():
    "A 3-element tuple of double-precision values."
    prefix = "Cart3d."
    enumx = (0, 1, 2)       # enumeration of indices
    zeros = [ 0.0, 0.0, 0.0 ]

    def __init__(self, *args) -> None:
            acnt = len(args)    # argument count
            if acnt == 0:
                # no args, fill with zeros
                self.elems = ar.array('d', Cart3d.zeros)
            elif acnt == 1:
                if isinstance(args[0], list) and len(args[0]) == 3:
                    # list comprised of 3 floats
                    self.elems = ar.array('d', args[0])
                elif isinstance(args[0], Cart3d):
                    # Cart3d
                    self.elems = args[0].elems
                else:
                    raise TypeError('Cart3d __init__ unknown argument')
            elif acnt == 3 and isinstance(args[0], float):
                # 3 floats
                self.elems = ar.array('d', args)
            else:
                raise TypeError('Cart3d __init__ unrecognized args count')

    def __repr__(self):
        return Cart3d.prefix+self.elems.__repr__()

    def __add__(self, other):
        # Cart3d + Cart3d
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] + other.elems[i]
        return c

    def __sub__(self, other) :
        # Cart3d - Cart3d
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] - other.elems[i]
        return c

    def __mul__(self, other):
        c = Cart3d()
        if isinstance(other, float): 
            # Cart3d * float
            for i in Cart3d.enumx:
                c.elems[i] = self.elems[i] * other
            return c
        elif isinstance(other, Cart3d): 
            # Cart3d * Cart3d (dot product)
            s = 0.0
            for i in Cart3d.enumx:
                s += self.elems[i] * other.elems[i]
            return s

    def __truediv__(self, other):
        # Cart3d / float
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] / other
        return c

    def __iadd__(self, other):
        # Cart3d += Cart3d
        for i in Cart3d.enumx:
            self.elems[i] += other.elems[i]
        return self

    def __isub__(self, other):
        # Cart3d -= Cart3d
        for i in Cart3d.enumx:
            self.elems[i] -= other.elems[i]
        return self

    def __imul__(self, other):
        # Cart3d *= float
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] * other
        return c

    def __itruediv__(self, other):
        # Cart3d /= float
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] / other
        return c

    def fromlist(self, ll):
        assert len(ll) == 3
        self.elems = ar.array('d', ll)
