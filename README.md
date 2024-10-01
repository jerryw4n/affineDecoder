# Affine Cipher Decryption Tool

This repository provides a Python implementation to decrypt messages encrypted using the affine cipher. The affine cipher is a type of substitution cipher that encrypts text using a mathematical formula. The tool includes a decryption function and a brute-force method to decrypt text when the keys are unknown.

## Functions

### 1. `decrypt(cipher, a, b)`
Decrypts a ciphertext using the affine cipher decryption formula.

- **Parameters:**
  - `cipher` (string): The encrypted message.
  - `a` (int): The multiplicative key used during encryption.
  - `b` (int): The additive key used during encryption.

- **Returns:**
  - `ans` (string): The decrypted message in lowercase.

- **Decryption Steps:**
  1. Convert each character in the ciphertext to a numeric value (0-25).
  2. Use the modular inverse of `a` to decrypt each letter.
  3. Convert the numeric value back to a letter.

### 2. `bruteForce(cipher)`
Attempts to brute-force decrypt the ciphertext by trying all possible combinations of the keys `a` and `b`.

- **Parameters:**
  - `cipher` (string): The encrypted message.

- **Brute-force Process:**
  1. Loops through all valid values of `a` (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25).
  2. Loops through all possible values of `b` (0-25).
  3. Prints each decrypted result for every key combination.

### 3. `greatestCommon(a, b)`
Finds the greatest common divisor (GCD) of two numbers using the extended Euclidean algorithm.

- **Parameters:**
  - `a` (int): The first number.
  - `b` (int): The second number.

- **Returns:**
  - A tuple `(g, x, y)` where `g` is the GCD, and `x` and `y` are coefficients such that `a * x + b * y = g`.

### 4. `modInverse(a, m)`
Calculates the modular inverse of `a` modulo `m`, which is required for the decryption formula.

- **Parameters:**
  - `a` (int): The number to find the inverse for.
  - `m` (int): The modulus.

- **Returns:**
  - The modular inverse of `a` modulo `m`.
