run = True
off = False
while run != off:
    number = float(input("Enter a number to convert: "))
#Converting numbers from base to to base 2
    if number < 0:
        print("Please enter a positive valor.")
    else:
        calculatedNumber = number
        integer_part = int(number)
        fractional_part = number - integer_part

        binary_Int_Representation, binary_Frac_Representation = "", ""
        if calculatedNumber >= 1:
            while calculatedNumber >= 1:
                birest = int(calculatedNumber % 2)
                calculatedNumber /= 2
                binaryRepresentation = "".join(reversed(str(birest))) + binaryRepresentation if 'binaryRepresentation' in locals() else str(birest)
           
            binary_Int_Representation = binaryRepresentation
            print("The binary representation is: ", binary_Int_Representation)
        
            
        calculatedNumber = number
        if calculatedNumber < 1 and calculatedNumber > 0:
            binaryRepresentation = "0."
            while calculatedNumber > 0:
                calculatedNumber *= 2
                birest = int(calculatedNumber)
                binaryRepresentation += str(birest)
                calculatedNumber -= birest
            binary_Frac_Representation = binaryRepresentation[2:]
    
        print("The binary representation is: {}{:06f}".format(binary_Int_Representation, float(binary_Frac_Representation) / (2 ** 10)))
            

#Conventing numbers from base to to base 8

    calculatedNumber = number
    if calculatedNumber >= 1:
        while calculatedNumber >= 1:
        
            octalrest = int(calculatedNumber % 8)
            calculatedNumber /= 8
            octalRepresentation = "".join(reversed(str(octalrest))) + octalRepresentation if 'octalRepresentation' in locals() else str(octalrest)
        print("The octal representation is: ", octalRepresentation)
    
    calculatedNumber = number
    if calculatedNumber < 1 and calculatedNumber > 0:
        octalRepresentation = "0."
        while calculatedNumber > 0:
            calculatedNumber *= 8
            octalrest = int(calculatedNumber)
            octalRepresentation += str(octalrest)
            calculatedNumber -= octalrest
        print("The octal representation is: {:.10f}".format(float(octalRepresentation)))
           
            
#Conventing numbers from base to to base 16
    calculatedNumber = number
    if calculatedNumber >= 1:
        while calculatedNumber >= 1:
            hexrest = int(calculatedNumber % 16)
            if hexrest >= 10:
                hexrest = chr(hexrest - 10 + ord('A'))
            calculatedNumber /= 16
            hexRepresentation = "".join(reversed(str(hexrest))) + hexRepresentation if 'hexRepresentation' in locals() else str(hexrest)
        print("The hexadecimal representation is: ", hexRepresentation)
    
    calculatedNumber = number
    if calculatedNumber < 1 and calculatedNumber > 0:
        hexRepresentation = "0."
        while calculatedNumber > 0:
            calculatedNumber *= 16
            hexrest = int(calculatedNumber)
            if hexrest >= 10:
                hexrest = chr(hexrest - 10 + ord('A'))
            hexRepresentation += str(hexrest)
            calculatedNumber -= int(calculatedNumber)
        print("The hexadecimal representation is: {}".format(hexRepresentation))
        
    # Ask user if they want to convert another number
    cont = input("Do you want to convert another number? (yes/no): ").strip().lower()
    if cont != 'yes':
        run = False