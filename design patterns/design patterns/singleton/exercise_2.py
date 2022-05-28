# from unittest import TestCase
import unittest
var = unittest.TestCase()
def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not
    obj1 = factory()
    obj2 = factory()
    return id(obj1) == id(obj2)
    