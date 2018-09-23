#!/bin/bash
NOT_LETTER="\([^\w]*\)"
sed -e "s/${NOT_LETTER}Dummy${NOT_LETTER}/\1Smart\2/" \
    -e "s/${NOT_LETTER}dummy${NOT_LETTER}/\1smart\2/" \
    -e "s/\".*\(\/Smart.h\)/\"nodb\1/" \
    -e "s/ db\s\?/ nodb/" \
    $1
