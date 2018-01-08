# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from time import time

class Block:
    """
    """
    def __init__(self, data, index, prev_hash):
        """
        """
        self.__data      = data
        self.__index     = index
        self.__prev_hash = prev_hash
        self.__timestamp = time()

    def __str__(self):
        """
        """
        return '{}{}{}{}'.format (
            self.__data, 
            self.__index, 
            self.__prev_hash, 
            self.__timestamp
        )
