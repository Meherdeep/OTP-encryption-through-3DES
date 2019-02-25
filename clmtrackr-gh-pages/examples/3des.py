# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:33:18 2019

@author: Meherdeep Thakur
"""
from random import*
from Crypto.Cipher import DES3
from Crypto import Random

key = b'0101011111001100'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)

plaintext = '1 9 4 7 ' #padded with spaces so than len(plaintext) is multiple of 8
encrypted_text = cipher_encrypt.encrypt(plaintext)
print(encrypted_text)
cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
print(cipher_decrypt.decrypt(encrypted_text))
