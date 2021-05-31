"""
vector3d -- 3-element vector using double-precision elements.
"""

from cart3d import Cart3d
import array as ar

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

