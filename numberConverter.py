#Conventing numbers from base to to base 2
number = float(input("Enter a number to convert: "))
if number < 0:
    print("Please enter a positive valor.")
else:
    calculatedNumber = number
    while calculatedNumber >= 1:
        birest = int(calculatedNumber % 2)
        calculatedNumber /= 2
        binaryRepresentation = "".join(reversed(str(birest))) + binaryRepresentation if 'binaryRepresentation' in locals() else str(birest)
    print("The binary representation is: ", binaryRepresentation)

#Conventing numbers from base to to base 8

    calculatedNumber = number
    while calculatedNumber >= 1:
    
        octalrest = int(calculatedNumber % 8)
        calculatedNumber /= 8
        octalRepresentation = "".join(reversed(str(octalrest))) + octalRepresentation if 'octalRepresentation' in locals() else str(octalrest)
    print("The octal representation is: ", octalRepresentation)
    
#Conventing numbers from base to to base 16
    calculatedNumber = number
    while calculatedNumber >= 1:
        hexrest = int(calculatedNumber % 16)
        if hexrest >= 10:
            hexrest = chr(hexrest - 10 + ord('A'))
        calculatedNumber /= 16
        hexRepresentation = "".join(reversed(str(hexrest))) + hexRepresentation if 'hexRepresentation' in locals() else str(hexrest)
    print("The hexadecimal representation is: ", hexRepresentation)