"""
Python: Program to generate coupon code
        Using base64 module
        Using random module
"""
import os
import base64
import random
from math import floor


def secure_rand(length=8):
    token = os.urandom(length)
    return base64.b64encode(token)


def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        #slice_start=random.randint(0,len(code_chars)-1)
        #code+=code_chars[slice_start:slice_start+1]
        code += code_chars[floor(random.randint(0, len(code_chars) - 1))]

    return code


if __name__ == '__main__':
    print("Using Secure Random Function", secure_rand())
    print("Using Get Promo Code", get_promo_code(8))
