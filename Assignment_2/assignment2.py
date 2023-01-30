#!/usr/bin/env python3
"""
Assignment 2 Python file
Copy-and-paste your extended_euclid and modexp functions
from assignment 1
"""
import random
import math


def modexp(x, y, N):
	"""
	Input: Three positive integers x and y, and N.
	Output: The number x^y mod N
	"""
	if y == 0:
		return 1
	z = modexp(x, math.floor(y / 2), N)
	if y % 2 == 0:
		return z ** 2 % N
	else:
		return (x ** y) % N


def modexp1(x, y, N):
	"""
	Input: Three positive integers x and y, and N.
	Output: The number x^y mod N
	"""
	if N == 1:
		return 0
	for i in range(y - 1):
		x = (x * x) % N
	return x


# part (ii) for extended Euclid  -- fill in the code below


def extended_euclid(a, b):
	"""
	Input: Two positive integers a >= b >= 0
	Output: Three integers x, y, and d returned as a tuple (x, y, d)
			such that d = gcd(a, b) and ax + by = d
	"""
	if b == 0:
		return (1, 0, a)
	x, y, d = extended_euclid(b, a % b)
	return y, x - (a // b) * y, d


def primality(N):
	"""
	Test if a number N is prime using Fermat's little Theorem with
	ten random values of a.  If a^(N-1) mod N = 1 for all values,
	then return true.  Otherwise return false.
	Hint:  you can generate a random integer between a and b using
	random.randint(a,b).
	"""
	for _ in range(10):
		a = random.randint(1, N - 1)
		if modexp(a, N - 1, N) != 1:
			return False
	return True


def prime_generator(N):
	"""
	This function generates a prime number <= N
	"""
	for _ in range(1000):
		p = random.randint(2, N)
		if primality(p):
			return p
	print("No prime found")
	return 0


def main():
	"""
	Test file for the two parts of the question
	"""
	# Excercise 1:  generating primes and RSA
	##################
	d = 0
	while d != 1:
		p = prime_generator(10000000)
		q = prime_generator(10000000)  # 10000000
		N = p * q
		e = 5
		x = 152  # 2148321
		a, b, d = extended_euclid(e, (p - 1) * (q - 1))
	decrypt = a % ((p - 1) * (q - 1))
	print("x", x)
	encoded = pow(x, e, N)
	decoded = pow(encoded, decrypt, N)
	#encoded = modexp(x, e, N)
	#decoded = modexp(encoded, decrypt, N)
	print("decoded: ", decoded)
	if x != decoded:
		print("Error")
		print(p)
		print(q)


if __name__ == '__main__':
	main()
