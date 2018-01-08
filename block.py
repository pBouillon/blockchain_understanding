# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from time import time

class Block:
    """Reference Block

    Blockchain block

    Attributes:
        __data  : content of the block, its value
        __index : position of the block
        __prev_hash : hash of the previous block
        __timestamp : current timestamp
    """
    def __init__(self, data, index, prev_hash):
        self.__data      = data
        self.__index     = index
        self.__prev_hash = prev_hash
        self.__timestamp = time()

    def __str__(self):
        """Get informations

        Returns:
            A string as {data}{index}{prev_hash}{timestamp}
        """
        return '{}{}{}{}'.format (
            self.__data, 
            self.__index, 
            self.__prev_hash, 
            self.__timestamp
        )
