#!/usr/bin/env python3
# tests for Point3d

import pytest
from point3d import Point3d
import array as ar

def test_init_nil():
    pnil = Point3d()
    assert pnil.elems == ar.array('d', [0, 0, 0])

def test_init_singlelist():
    p1 = Point3d([1.0, 2.0, 3.0])
    assert p1.elems == ar.array('d', [1.0, 2.0, 3.0])

def test_init_3args():
    p3 = Point3d(6.1, 6.2, 6.3)
    assert p3.elems == ar.array('d', [6.1, 6.2, 6.3])

def test_distanceSquared():
    p1 = Point3d(3.0, 0.0, 0.0)
    p2 = Point3d(0.0, 4.0, 0.0)
    assert p1.distanceSquared(p2) == 25

def test_distance():
    p1 = Point3d(3.0, 0.0, 0.0)
    p2 = Point3d(0.0, 4.0, 0.0)
    assert p1.distance(p2) == 5

