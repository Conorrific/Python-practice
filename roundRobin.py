import calculatornotes


def displayResult(a,b,c,d):
    print("*************************")
    print(f"{first_number} {operand} {second_number} = {result}")
    print("*************************")
def askForUserInput():
    first_number = float(input("Enter first number: "))
    operand = input("Enter operand")
    second_number = float(input("Enter second number: "))
    return first_number,operand,second_number
(first_number,operand,second_number) = askForUserInput()
#initialize result to 0.0 so that it won't begin with a null or nothing answer.
#zero is different than null
result = 0.0

if operand == "+":
    result = calculatornotes.add(first_number,second_number)
elif operand == "-":
    result = calculatornotes.sub(first_number,second_number)
#Why is this still throwing an error?
#sumthin funny here.. it aint workin. giving an operand error trying to convert it to float or to 
displayResult(first_number,second_number,operand,result)