# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:18:51 2019

@author: hp
"""

import electronic_code_book as ecb
import cipher_feed_back as cfb
import cipher_block_chaining as cbc
import output_feed_back as ofb
dic = {}
dic['ecb'] = ecb
dic['cfb'] = cfb
dic['cbc'] = cbc
dic['ofb'] = ofb
def get_mode(mode_name):
    return dic[mode_name.lower()]