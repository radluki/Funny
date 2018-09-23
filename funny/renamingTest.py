#!/usr/bin/env python3
import unittest
from renaming import *


class RenamerTest(unittest.TestCase):

    def setUp(self):
        self.sub = Renamer("OldClass", "NewClass")
        self.singleOccuranceStr = "     \tOldClass \toldClass"
        self.newClassStr = "     \tNewClass \toldClass"
        self.doubleOccuranceStr = self.singleOccuranceStr*2
        self.newClassesStr = self.newClassStr*2
        self.newObjectStr = "     \tOldClass \tnewClass"
        self.newObjectsStr = self.newObjectStr*2

    def assert_substitute(self, old, new, fun):
        self.assertEqual(new, fun(old), "String after substitution is incorrect")

    def test_substitute_class_name_single(self):
        self.assert_substitute(self.singleOccuranceStr, self.newClassStr, self.sub.substitute_class_name)

    def test_substitute_class_name_double(self):
        self.assert_substitute(self.doubleOccuranceStr, self.newClassesStr, self.sub.substitute_class_name)

    def test_substitute_object_name_single(self):
        self.assert_substitute(self.singleOccuranceStr, self.newObjectStr, self.sub.substitute_object_name)

    def test_substitute_object_name_double(self):
        self.assert_substitute(self.doubleOccuranceStr, self.newObjectsStr, self.sub.substitute_object_name)

    def test_substitute_class_name_include(self):
        string = "#include \"msg/db/OldClass.h\""
        newString = "#include \"msg/db/OldClass.h\""
        self.assert_substitute(string, newString, self.sub.substitute_class_name)


if __name__=='__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RenamerTest)
    unittest.TextTestRunner().run(suite)
