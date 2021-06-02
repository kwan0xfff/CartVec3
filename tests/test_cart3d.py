#!/usr/bin/env python3
# tests for Cart3d

import pytest
from cart3d import Cart3d
import array as ar

def test_init_nil():
    cnil = Cart3d()
    assert cnil.elems == ar.array('d', [0, 0, 0])

def test_init_singlelist():
    c1 = Cart3d([1.0, 2.0, 3.0])
    assert c1.elems == ar.array('d', [1.0, 2.0, 3.0])

def test_init_3args():
    c3 = Cart3d(6.1, 6.2, 6.3)
    assert c3.elems == ar.array('d', [6.1, 6.2, 6.3])

def test_init_Cart3d():
    c1 = Cart3d([1.0, 2.0, 3.0])
    c2 = Cart3d(c1)
    assert c1.elems == c2.elems

def test_init_2args_raise():
    with pytest.raises(TypeError):
        c2 = Cart3d([1.5, 2.5])

def test_init_strs_raise():
    with pytest.raises(TypeError):
        c1x = Cart3d(["one", "two", "three"])

def test_elems_ne():
    c123 = Cart3d([1.0, 2.0, 3.0])
    c234 = Cart3d([2.0, 3.0, 4.0])
    assert c123.elems != c234.elems

def test_add():
    c123 = Cart3d([1.0, 2.0, 3.0])
    c111 = Cart3d([1.0, 1.0, 1.0])
    csum = c123 + c111
    assert csum.elems == ar.array('d',[2.0, 3.0, 4.0])

def test_sub():
    c123 = Cart3d([1.0, 2.0, 3.0])
    c111 = Cart3d([1.0, 1.0, 1.0])
    cdif = c123 - c111
    assert cdif.elems == ar.array('d',[0.0, 1.0, 2.0])

def test_mul_c3_sc():
    c123 = Cart3d([1.0, 2.0, 3.0])
    cresult = c123 * 2.0
    assert cresult.elems == ar.array('d',[2.0, 4.0, 6.0])

def test_mul_c3_c3():
    c123 = Cart3d([1.0, 2.0, 3.0])
    c222 = Cart3d([2.0, 2.0, 2.0])
    cresult = c123 * c222
    assert cresult == 12

def test_truediv():
    c123 = Cart3d([1.0, 2.0, 3.0])
    cdiv = c123 / 2.0
    assert cdiv.elems == ar.array('d',[0.5, 1.0, 1.5])

def test_iadd():
    csum = Cart3d([1.0, 2.0, 3.0])
    c111 = Cart3d([1.0, 1.0, 1.0])
    csum += c111
    assert csum.elems == ar.array('d',[2.0, 3.0, 4.0])

def test_isub():
    cdif = Cart3d([1.0, 2.0, 3.0])
    c111 = Cart3d([1.0, 1.0, 1.0])
    cdif -= c111
    assert cdif.elems == ar.array('d',[0.0, 1.0, 2.0])

def test_imul():
    cccc = Cart3d([1.0, 2.0, 3.0])
    cccc *= 2.0
    assert cccc.elems == ar.array('d',[2.0, 4.0, 6.0])

def test_itruediv():
    cccc = Cart3d([1.0, 2.0, 3.0])
    cccc /= 2.0
    assert cccc.elems == ar.array('d',[0.5, 1.0, 1.5])

def test_fromlist():
    c246 = Cart3d()
    c246.fromlist([2, 4, 6])
    assert c246.elems == ar.array('d', [2, 4, 6])


