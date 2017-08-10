#!/usr/bin/env python
def to_bin(dec):
    flag = True
    bin_str = ''
    while flag:
        remainder = dec % 2
        quotient = dec / 2
        if quotient == 0:
            flag = False
        bin_str += str(remainder)
        dec = quotient
    print bin_str    
    bin_str = bin_str[::-1] # reverse the string
    return bin_str
dec = int(raw_input("enter dec:"))
to_bin(dec)
print to_bin(dec)
