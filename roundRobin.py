import calculatornotes

#The stuff inside the () below is arpitrary. It just has to show that there are 
#four places being used or however many you need. 
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

displayResult(first_number,second_number,operand,result)