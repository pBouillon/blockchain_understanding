# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import block
from block import Block

import hashlib
from hashlib import sha256


""" """
CONSTRAINT = '0000'

""" """
GENESIS_DATA = 'Hello Blockchain !'


class Blockchain:
    """
    """
    def __init__(self):
        self.__blocks = []
        self.__init_blockchain()

    def __create_block(self, data, genesis=0):
        """
        """
        previous = 0
        if not genesis:
            previous = self.__blocks[::-1][0]

        block = Block (
                    data, 
                    len(self.__blocks),
                    previous
                )

        _hash  = ''
        adjust = 0
        while not self.__valid(_hash):
            core = '{}{}'.format(block, adjust)
            _hash_obj = sha256(core.encode())
            _hash = _hash_obj.hexdigest()
            adjust += 1

        print('Block took {} tries to be generated.'.format(adjust-1))
        self.__blocks.append(_hash)

    def __init_blockchain(self):
        """
        """
        self.__create_block(GENESIS_DATA, 1)

    def __valid(self, _hash):
        """
        """
        return _hash.startswith(CONSTRAINT)

    def add_block(self, data):
        """
        """
        self.__create_block(data)

    def get_blockchain(self):
        """
        """
        return self.__blocks

