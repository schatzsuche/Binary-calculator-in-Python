number = 0
try: number = int(input("Enter the number you want to convert to Binary : "))

except:
    print("sorry that is not a valid number")
binary = ''
test = number
while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2
    
print("The binary from " + str(test) + " " + "is:", binary)
