# Comments are made by a human being not an AI, I wanted to make sure I understand the whole program!

import hashlib as h # Importing the main python library for working with hashes.
import os # Importing Operating System library for creating random messages of 16 bytes.
import time # Importing Time for the calculation of duration of the tests.

def sha256_trunc_bits(m: bytes, t: int) -> int: # Define the function for creating and truncing hashes. 
    fullHash = h.sha256(m).digest() # Created SHA256 Hash and storing to variable #fullHash.
    bigNum = int.from_bytes(fullHash, byteorder='big') # Ensures bytes get sorted correctly from left to right -> parameter (#byteorder='big').
    strippedHash = bigNum >> (256 - t) # Removes all bytes apart from the "t" specified, starting from the right.
    
    return strippedHash # Returns final bytes.

"""
print(sha256_trunc_bits(b"Ahoj", 8)) # Test return #1 -> Should return less than 256.
print(sha256_trunc_bits(b"Svete", 8)) # Test return #2 -> Should return less than 256.
print(sha256_trunc_bits(b"Python", 8)) # Test return #3 -> Should return less than 256.
"""

def find_colision(t): # Define function that seeks colisions.
    startTime = time.time() # Determine start time of seeking for the colisions.
    endTime = 0 # Predetermine ending time.
    seen = {} # Define a dictionary for the hashes.
    attempts = 0 # Define a variable for number of attempts. 

    while True:
        attempts += 1 # Start a new attempt.
        m = os.urandom(16) # Generates a random message that contains 16 bytes.
        h = sha256_trunc_bits(m, t) # Hashing the previously created random message "m" and truncing it by parameter "t".
        if h in seen: # Seeking for already existing hash.
            if seen[h] != m: # Confirming that it is not a duped hash (Not likely, but we need to make sure).
                endTime = time.time() - startTime # Calculating the ending time.
                m0 = seen[h] # Getting the original message.
                return attempts, endTime, m, m0, h # Returning number of attempts, duration, current and original messages, hash. 
        else:
            seen[h] = m # Storing the new discovered message to the dictionary.

testValues = [16, 20, 24, 28, 32] # Defining a list with the values determined for truncing, from assesment. 

def test_values(testValues): # Define the main test function.
    
    for t in testValues: # For-cycle for looping through the attempts and then printing it out.
        attempts, time, currentMessage, originalMessage, colisionHash = find_colision(t) # Getting the values from our find_colision() function.

        print(f"--- t = {t} ---") # Tested "t" parameter.
        print(f"Attempts: {attempts}") # Number of attempts.
        print(f"Time: {time:.4f} s") # Duration of current test.
        print(f"Current message (hex): {currentMessage.hex()}") # The current message.
        print(f"Original message (hex): {originalMessage.hex()}") # Original message from the dictionary seen{}.
        print(f"Trunced hash: {colisionHash}") # Printing out the trunced hash.
        print() # Just an empty line lol, cosmetics reasons.

    print(f"{'t':<5} | {'Theory (50%)':<15} | {'Realtime (attempts)':<18} | {'Time (s)':<10}") # Printing the format of the table from the assesment # C #.
    print("-" * 55) # Printing "-" 55 times just because it's cool lol.

    for t in testValues: # Looping through all the values sorted in testValues[].
        attempts, time, currentMessage, originalMessage, colisionHash = find_colision(t) # Accessing the values from our find_colision() function.
        
        theory = 1.1774 * (2 ** (t / 2)) # Calculation of the Theory.

        print(f"{t:<5} | {int(theory):<15} | {attempts:<18} | {time:.4f}") # Printing one line of the table, parsing "Theory" to int, so that we have don't have floats lol.

test_values(testValues) # Calling the function for the test of values determined by testValues[] list.

