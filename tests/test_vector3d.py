#!/usr/bin/env python3
# tests for Vector3d

import pytest
from vector3d import Vector3d
import array as ar

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
