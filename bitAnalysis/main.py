import math # Importing math for easier access to logarithms.

a='1111101101011110011111101100010111001010101111110111111011111011001100001001111110111101110110111101011001111101001101101010101111111101011110101110111110111111111111100011111101101111110111111110101010100101111110011101111110110101010000110101011110110100000110101001010111100110101111110111100111111111001111111110011011111111101110110101110000100111110111111001111011101101111111010111010111010111111111111111111111111011101100101110011011111000101111111111011110111110011000011011011010111110111111010101011101111010111111011001111110001111111001101001001110010111000110110111010011111111100011011111111001111101110111011010110100111111111111011110011001110011111111110111011100000100011110011001111111011111110001101111101111111111001111011111010110010011101110110101111110101110111010111011011100011011011101110010001100111111111111001011000001010101011001111011111110011111111011110001101011101011011111111011010111001100101001101110111111101111111001111111111111011100110111111111111101101110' # First sequence from lejstro.
b='0111010000110010101101000000010001011100100111110011100110110101111010101100000000101110100110100110110010001111100011101001001001001100110110010011001110000100111111000111100110110100110111110001010101000110001010100101100101100011000000010111111110110001010111111101111111011010110100000010100111001010010010010110110011110010110100010100000010011000110101101010100110010000011111010101000010100000101010011100110101011101101000010111001001001110100000100110011010000111010010001001110101111101100111100011010110010101111001111011111100001110101001111111001100101100111110111011111111111000100101011000011000000011000010011010101001011010011100011110011110101111011111111111000000110111110001000110010011111001000001101111101101110000001110100010101011111011110100111011111100010010110000001010000111010111110011111100101101111100111001001110111001110011110000110000000100000100100110011101111100111111001111111000011101111111011111110001011101100111011111001110111011101000110111111111100101011110' # Second sequence from lejstro.

def vonNeumann(sequence): # Define function for vonNeumann method.
    correctedSeq = '' # Define corrected sequence, blank, for easier work.
    for i in range(0, len(sequence) - 1, 2): # Looping through the sequence.
        pair = sequence[i:i+2] # Take the original long sequence, go for the position 'i' and slice it to the position 'i+2'.

        if pair == "01": # Is there a pair '01'.
            correctedSeq += "0" # Append this to the existing.
        elif pair == "10": # Is there a pair '10'.
            correctedSeq += "1" # Append this to the existing.

    return correctedSeq # Return corrected sequence.

def analyseSeq(sequence, name): # Define function for analysing the sequences.
    lengthSeq = len(sequence) # Check the length of the sequence.
    countNum0 = 0 # Declare a variable for count of '0'.
    countNum1 = 0 # Declare a variable for count of '1'.

    for i in range(lengthSeq): # Loop through the sequence.
        if sequence[i] == '1': # Checks for the slice of the sequence.
            countNum1+=1 # Adds one to the count of '1's.
        elif sequence[i] == '0': # Checks for the slice of the sequence.
            countNum0+=1 # Adds one to the count of '0's.

    likelihood0 = countNum0 / lengthSeq # Count the likelihood for 'O'.
    likelihood1 = countNum1 / lengthSeq # Count the likelihood for '1'.

    if likelihood0 == 0 or likelihood1 == 0: # Checks for condition of '0' for Shannon Entropy.
        shannon_entropy = 0 # Sets Shannon Entropy to '0'.
    else: 
        shannon_entropy = -(likelihood0 * math.log2(likelihood0) + likelihood1*math.log2(likelihood1)) # Otherwise calculates the Shannon Entropy by the formula.

    minEntropy = -(math.log2(max(likelihood0, likelihood1))) # Calculates the Min-Entropy by the formula.

    s = countNum1 - countNum0 # Calculates 's' pretty simply.
    sObs = abs(s)/math.sqrt(lengthSeq) # Calculates 's_obs' pretty simply.

    print(f'--- Sequence: {name} ---') # Formatting the sequence results.
    print(f'Length (n): {lengthSeq}') # Prints out the length.
    print(f'Number of zeros (n0): {countNum0}') # Prints the number of zeros.
    print(f'Number of ones (n1): {countNum1}') # Prints the number of ones.
    print(f'P(0) = {likelihood0}') # Prints the likelihood of '0's.
    print(f'P(1) = {likelihood1}') # Prints the likelihood of '1's.
    print(f'Shannon Entropy: {shannon_entropy}') # Prints the result of Shannon Entropy.
    print(f'Min-Entropy: {minEntropy}') # Prints the result of MinEntropy.
    print(f'S_obs (Monobit): {sObs:.4f}') # Prints the Results of S in monobit.

    if 0.45 <= likelihood0 <= 0.55: # Checks whether the sequence is balanced.
        print("Result: Sequence is most likely BALANCED.") # Returns that the sequence is balanced.
    else: # Checks whether the unsequence is balanced.
        print("Resul: Sequence is most likely BIAS (UNBALANCED).") # Returns that the sequence is unbalanced.

    if sObs <= 2.58: # Checks whether the sequence passes. 
        print("Result: Sequence is most likely ACCEPTABLE.") # Returns that the sequence is acceptable.
    else: #  Checks whether the sequence does not pass. 
        print("Result: Sequence is most likely SUSPICIOUS.") # Returns that the sequence is unacceptable.
    print() # Empty line for formatting.

    return lengthSeq, countNum0, countNum1, likelihood0, likelihood1 # Returns all needed variables.

analyseSeq(a, 'A - Original') # Calling the function for analysing the 'A' sequence.
analyseSeq(b, 'B - Original') # Calling the function for analysing the 'B' sequence.

correctedA = vonNeumann(a) # Correcting the 'A' sequence according to vonNeumann's method.
correctedB = vonNeumann(b) # Correcting the 'B' sequence according to vonNeumann's method.


analyseSeq(correctedA, 'A - Von Neumann') # Calling the function for analysing the vonNeumann-modified 'A' sequence.
analyseSeq(correctedB, 'B - Von Neumann') # Calling the function for analysing the vonNeumann-modified 'B' sequence.