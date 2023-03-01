#!/usr/bin/env python3
"""
ECE 406:  File for Exercise 1 of Assignment #3
"""
import numpy.fft as np


def poly_eval(coeff, x):
    p = 0
    for i, c in enumerate(coeff):
        p += c * x**i
    return p


def my_fft(a, b, Acoeff, Bcoeff):
    """
    Exercise 1:  Using the FFT to multiply two binary numbers.
    You just need to fill in parts (v) and (vi)
    """
    # The binary numbers and their product
    c_bin = a_bin * b_bin
    print('\n(true answer) The product of a, (', bin(a_bin), '=',
          a_bin, ') and b, (', bin(b_bin), '=', b_bin, ') is', c_bin)

    # (i) The coefficients of the polynomials A and B (see main)
    print_opt('Acoeff=', Acoeff)
    print_opt('Boeff=', Bcoeff)

    # (ii) the value representations of A and B
    Aval = np.fft(Acoeff, 32)
    Bval = np.fft(Bcoeff, 32)

    print_opt('(ii) Aval=', Aval)
    print_opt('(ii) Bval=', Bval)

    # (iii) The value representation of C
    Cval = []
    for i in range(len(Aval)):
        Cval.append(Aval[i] * Bval[i])

    print_opt('(iii) Value representation of C(x)=A(x)B(x) from FFT', Cval)

    # (iv) The coefficients of the polynomial C
    Ccoeff = np.ifft(Cval)
    # we'll get rid of the imaginary parts, which are just numerical errors
    for i, c in enumerate(Ccoeff):
        Ccoeff[i] = int(round(c.real))

    print('(iv) Coefficient representation of C(x)', Ccoeff.real)

    # (v) calculate the product by evaluating the polynomial at 2, i.e., C(2)
    # (You may need to take the real part at the end if there is a small imaginary component)

    # evalute polynomial from its coefficients

    prod = poly_eval(Ccoeff, 2)
    print('(v) Using the FFT the product of a and b is', int(round(prod.real)))

    # (vi) write code to calculate the binary digits of c directly from the coefficients of C, Ccoeff.

    c = bin(int(round(prod.real)))
    print('(vi) (bit-array) bits of binary array c=', c)

    # print the binary number

    c_bin = bin(int(round(prod.real)))
    print("(vi) (binary) The product of a and b in binary is", c_bin)

    # finally, check that c_string is the correct binary number
    c_dec = int(c_bin, 2)
    print("(vi) (binary-to-decimal) The conversion of this binary number to decimal is", c_dec)


def print_opt(*args, **kwargs):
    '''Print out a string if the PRINT_OPT flag is TRUE. (DO NOT CHANGE THIS OR USE IT FOR PRINTING FINAL ANSWERS, IT IS ONLY FOR REDUCING CLUTTER DURING THE GRADING)'''
    if PRINT_OPT:
        print(*args, **kwargs)


if __name__ == '__main__':
    global PRINT_OPT
    PRINT_OPT = True
    a_bin = 0b110000001101
    b_bin = 0b100011110001
    Acoeff = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    Bcoeff = [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]
    my_fft(a_bin, b_bin, Acoeff, Bcoeff)
