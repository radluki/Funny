#!/usr/bin/env python3
import re
import argparse


class Renamer:

    def __init__(self, class_name, new_class_name):
        self.old_class_name = class_name
        self.new_class_name = new_class_name
        self.__not_word = r"([^\w/]+)"
        self.__not_word_or_nothing = r"([^\w]*(.h)?;?)"

    @staticmethod
    def first_letter_to_lower(word):
        return word[0].lower() + word[1:]

    def substitute_word(self, line, old_word, new_word):
        return re.sub(self.__not_word + old_word + self.__not_word_or_nothing,
               r"\1" + new_word + r"\2", line)

    def substitute_class_name(self, line):
        return self.substitute_word(line, self.old_class_name, self.new_class_name)

    def substitute_object_name(self, line):
        objName = self.first_letter_to_lower(self.old_class_name)
        newObjName = self.first_letter_to_lower(self.new_class_name)
        return self.substitute_word(line, objName, newObjName)


class MyParser(argparse.ArgumentParser):

    def __init__(self):
        super().__init__(description="Rename c++ class in file.")
        self.add_argument("file")
        self.add_argument('oldClassName')
        self.add_argument('newClassName')


if __name__=='__main__':
    parser = MyParser()
    args = parser.parse_args()
    renamer = Renamer(args.oldClassName, args.newClassName)
    with open(args.file, 'r') as f:
        for line in f:
            line = renamer.substitute_class_name(line)
            line = renamer.substitute_object_name(line)
            print(line, end='')
