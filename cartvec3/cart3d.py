"""
cart3d -- Cartesian coordinates, 3 axes, double-precision
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
                self.elems = ar.array('d', Cart3d.zeros)
            elif acnt == 1 and isinstance(args[0], list) and len(args[0]) == 3:
                self.elems = ar.array('d', args[0])
            elif acnt == 3 and isinstance(args[0], float):
                self.elems = ar.array('d', args)
            else:
                raise TypeError('Cart3d __init__ unrecognized args count')

    def __repr__(self):
        return Cart3d.prefix+self.elems.__repr__()

    def __add__(self, other) :
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] + other.elems[i]
        return c

    def __sub__(self, other) :
        c = Cart3d()
        for i in Cart3d.enumx:
            c.elems[i] = self.elems[i] - other.elems[i]
        return c

    def __iadd__(self, other):
        for i in Cart3d.enumx:
            self.elems[i] += other.elems[i]
        return self

    def __isub__(self, other):
        for i in Cart3d.enumx:
            self.elems[i] -= other.elems[i]
        return self

    def fromlist(self, ll):
        assert len(ll) == 3
        self.elems = ar.array('d', ll)
