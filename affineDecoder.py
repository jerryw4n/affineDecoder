# Function for the process of decryption
def decrypt(cipher, a, b):
	ans = ""
	numval = 0
	modinv = modInverse(a, 26)

	# Loop for each character in the cipher
	for x in cipher:
			# Get numeric value
			numval = ord(x)
			# Scale 0 to 25
			numval = numval - ord('A')
			# Get plaintext as numeric value
			numletter = modinv * (numval - b) % 26
			# Map back to a character in the ASCII value then add 'A' to convert to character
			ans += chr(numletter + ord('A')).lower()

	return ans

def bruteForce(cipher):
	# All possible combinations of a and b for affine
	x = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
	y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

	# Loop for every possible combination
	for i in range(0, len(x)):
		a = x[i]
		for j in range(0, len(y)):
			b = y[j]
			print(f"Key: a = {a} a = {b}")
			# Each time the decoder is finished, print it out to see the result
			print(f"{decrypt(cipher=cipher, a=a, b=b)}\n")

# Function for finding the greatest common divisor for a and b 
def greatestCommon(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = greatestCommon(b % a, a)
	return (g, x - (b // a) * y, y)

# Function for getting the inverse of the current mod
def modInverse(a, m):
	g, x, y = greatestCommon(a, m)
	return x % m

# Invokes all the functions to run the program
cipher = input("Enter the sentence you want to decode: ").upper()
print("")
bruteForce(cipher)