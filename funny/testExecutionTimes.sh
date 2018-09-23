#!/usr/bin/env bash

TEST_FILE="../testData/python/DummyTest.cpp"
time ./renamer.sh ${TEST_FILE} > renamer.out
time ./renaming.py ${TEST_FILE} Dummy Smart > renaming.out