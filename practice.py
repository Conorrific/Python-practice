##create array of numbers, and have user search for numbers in the array.
## if they guess it then print number {} is at index{}
#number = 7
#guesses = 0
#guess = int(input("Guess a number from '1' to '10'"))
##def endGame():
#   # print("Winner Winner Chicken Dinner! ")
#    #break
##def playGame():
#for i in number:
#    if guess != number and guesses <= 5:
#        print("guess again! ")
#        guesses += 1
#    elif guess == number or guesses > 5:
#        print("Sorry, invalid ")        

numbers = [10,20,30,5]
number_to_search = int(input("Enter your number to search: "))

for index in range(0, len(numbers)):
    if number_to_search == numbers[index]:
        print("Found!")
        break
    else:
        print("Not found!")
