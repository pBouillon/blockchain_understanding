# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import block
from block import Block

import hashlib
from hashlib import sha256

""" Blockain difficulty """
DIFFICULTY = '0000'

""" Data in the genesis block """
GENESIS_DATA = 'Hello Blockchain !'

class Blockchain:
    """Reference Blockchain

    Basic blockchain
    Create its first block on initialization

    Attributes:
        __blocks : table of all blocks hash
    """
    def __init__(self):
        self.__blocks = []
        self.__init_blockchain()

    def __create_block(self, data, genesis=0):
        """Create a new block in the blockchain

        Create a block
        Generate its hash
        If it is valid, add its hash to __blocks

        Parameters:
            data    : block content
            genesis : 0 if normal block
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
        """Generate the genesis
        """
        self.__create_block(GENESIS_DATA, 1)

    def __valid(self, _hash):
        """Chech hash validity

        Check if the hash is matching the DIFFICULTY

        Parameters:
            _hash : generated hash

        Returns:
            1 if valid, 0 otherwise
        """
        return _hash.startswith(DIFFICULTY)

    def add_block(self, data):
        """Add a new block

        Parameters:
            data : block content
        """
        self.__create_block(data)

    def get_blockchain(self):
        """Get the blockchain

        Returns:
            __blocks : the blockchain
        """
        return self.__blocks

