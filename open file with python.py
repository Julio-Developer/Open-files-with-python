#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    with open('file.txt', encoding='utf-8') as file:
        for read in file:
            print (read)
except FileNotFoundError:
    print('File Note Found')
except:
    print('Error Unexpected')