# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import blockchain
from blockchain import Blockchain

def format_bc(blockchain):
    """Formats the output of the blockchain
    """
    for block in blockchain:
        print(block)

if __name__ == '__main__':
    bc = Blockchain()
    format_bc(bc.get_blockchain())

    bc.add_block('test')
    bc.add_block('test 2')
    bc.add_block('test 3')
    format_bc(bc.get_blockchain())
