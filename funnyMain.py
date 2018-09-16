import os
import numpy as np
import re
import unittest
from unittest.mock import MagicMock


class FunnyObject:

    def __init__(self, left=1, right=2):
        print("Hello I'm funny")
        self.left = left
        self.right = right

    def __str__(self):
        return "FunnyObject(left: " + str(self.left) \
            + ", right: " + str(self.right) + ")"

    def __repr__(self):
        return "<" + str(self) + " at " + str(id(self)) + ">"

    def get_random_value(self):
        return self.left*23

    @classmethod
    def funny_class_method(cls, string):
        print("Funny string: ", string)

    @classmethod
    def modify_file(cls):
        files = [os.path.join(current, fi) for current, _, files in os.walk('.') for fi in files]
        for name in files:
            if name != os.path.join(r'.', r'testingFile.txt'):
                continue
            with open(name, 'r') as f, open('out.txt', 'w') as w:
                for line in f:
                    pattern = re.compile(r'(\w+\W+)')
                    matches = re.findall(pattern, line)
                    string = 'xxx '.join(matches)
                    w.write(string)


class FunnyObjectTest(unittest.TestCase):

    def setUp(self):
        self.funnyObject = FunnyObject()

    def test_repr(self):
        pattern = re.compile(r'<FunnyObject\(left: 1, right: 2\) at \d+>')
        self.assertTrue(pattern.match(self.funnyObject.__repr__()))

    def test_repr3(self):
        self.assertNotEqual(FunnyObject(), self.funnyObject)

    def test_get_random_value(self):
        self.assertEqual(23, self.funnyObject.get_random_value())
        self.funnyObject.get_random_value = MagicMock(return_value=100)
        self.assertEqual(100, self.funnyObject.get_random_value())
        print(self.funnyObject.get_random_value.assert_called())


# import importlib
# importlib.reload(moduleName)


if __name__ == '__main__':
    print(os.listdir(r'.'))
    print('Hello World')
    a = np.asarray([[[1, 2], [3, 1]], [[1, 1], [2, 2]]])
    print(a)
    funny = FunnyObject()
    print(funny)
    funny = FunnyObject(6, 9)
    print(funny)
    iter = os.walk('.')
    print(iter)
    print(next(iter))
    print(next(iter))
    print(next(iter))
    FunnyObject.funny_class_method("HAHAHA")
    FunnyObject.modify_file()
    unittest.main()
