#!/usr/bin/env python3
# tests for Vector3d

import pytest
from vector3d import Vector3d, normalize
import array as ar
import math

def test_init_nil():
    vnil = Vector3d()
    assert vnil.elems == ar.array('d', [0, 0, 0])

def test_init_singlelist():
    v1 = Vector3d([1.0, 2.0, 3.0])
    assert v1.elems == ar.array('d', [1.0, 2.0, 3.0])

def test_init_3args():
    v3 = Vector3d(6.1, 6.2, 6.3)
    assert v3.elems == ar.array('d', [6.1, 6.2, 6.3])

def test_matmul():
    v1 = Vector3d(1.0, 0.0, 0.0)
    v2 = Vector3d(0.0, 1.0, 0.0)
    v3 = v1 @ v2
    assert v3.elems == ar.array('d', [0.0, 0.0, 1.0])

def vectordiff(v1, v2):
    v0 = Vector3d()
    v0 = v1 - v2
    s = v0*v0
    assert isinstance(s, float)
    return s

def test_normalize_nonclass():
    v1 = Vector3d(3.0, 4.0, 5.0)
    v2 = Vector3d()
    vnormx = Vector3d(0.424264068711928,0.565685424949238,0.7071067811865475)
    v2 = normalize(v1)
    assert vectordiff (v2, vnormx) < 1.0e-10

def test_normalize():
    v1 = Vector3d(3.0, 4.0, 5.0)
    vnormx = Vector3d(0.424264068711928,0.565685424949238,0.7071067811865475)
    v1.normalize()
    assert vectordiff (v1, vnormx) < 1.0e-10

def test_lengthSquared():
    v1 = Vector3d(3.0, 4.0, 5.0)
    lsq = v1.lengthSquared()
    assert lsq == 50.0

def test_length():
    v1 = Vector3d(3.0, 4.0, 5.0)
    dist = v1.length()
    ref = 7.0710678118654755
    assert (abs(dist-ref)) < 1.0e-10

def test_angle():
    v0 = Vector3d(1.0, 0.0, 0.0)
    v1 = Vector3d(1.0, 1.0, 0.0)
    ref = math.pi/4.0
    a = v0.angle(v1)
    assert (abs(a-ref)) < 1.0e-10
    a = v1.angle(v0)
    assert (abs(a-ref)) < 1.0e-10

