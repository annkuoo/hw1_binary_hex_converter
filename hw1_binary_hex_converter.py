#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:57:29 2024

@author: annkuo
"""
# function for converting decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary if binary else "0"

# function for converting decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"
    while decimal > 0:
        hexadecimal = hex_chars[decimal % 16] + hexadecimal
        decimal //= 16
    return hexadecimal if hexadecimal else "0"

def main():
    while True:
        try:
            decimal = int(input("Please enter a decimal number (0-255):"))
            if 0 <= decimal <= 255:
                binary = decimal_to_binary(decimal)
                hexadecimal = decimal_to_hexadecimal(decimal)
                print(f"十進位數字 {decimal} 的二進位表示為: {binary}")
                print(f"十進位數字 {decimal} 的十六進位表示為: {hexadecimal}")
                break
            else:
                print("The decimal number must be between 0 and 255. Please try again.")
        except ValueError:
            print("Please enter a decimal number.")
            
if __name__ == "__main__":
   main()
