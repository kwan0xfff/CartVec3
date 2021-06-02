#!/usr/bin/env python3
# example: trajectory1.py

"""
Simple trajectory computation using the Cart3d class.

The trajectory is basically a parabola starting at the origin
and accelerating at one distance unit per time unit (e.g., 1 meter/sec).
The computation is shown for a one-step solution as well as multi-step .
In this case, the two solutions are identical since are basically computing
points on the parabola.
"""

from cart3d import Cart3d

c3zeros = Cart3d([0.0, 0.0, 0.0])

def step(x0, xd0, xdd0, dt):
    """Compute new position (x1) and velocity (xd1)from current
    position (x0), velocity (xd0), acceleration (xdd0), and stepsize (dt).
    """
    xd1 = xd0 + xdd0*dt
    x1 = x0 + xd0*dt + xdd0*(dt*dt)*0.5
    return x1, xd1

def onestep():
    pos0 = c3zeros
    velo0 = c3zeros
    accel = Cart3d([1.0, 0.0, 0.0])
    n = dt = 10.0
    pos1, velo1 = step(pos0, velo0, accel, dt)
    print(f"n {n} pos {pos1} velo {velo1}")


def multistep():
    pos0 = c3zeros
    velo0 = c3zeros
    accel = Cart3d([1.0, 0.0, 0.0])
    dt = 1.0
    n = 0
    print(f"n {n} pos {pos0} velo {velo0}")
    for n in range(1,11):
        pos1, velo1 = step(pos0, velo0, accel, dt)
        print(f"n {n} pos {pos1} velo {velo1}")
        pos0 = pos1
        velo0 = velo1

print("== onestep ==")
onestep()
print("== multistep ==")
multistep()
