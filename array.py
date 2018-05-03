



names = ["John","Alex","Mary","Steve","Jerry","Krammer","George"]
#make the array name plural so that it sounds more natural
numbers = [34,56,12,78,56,687]

names.append("Some name")

#remove from array
names.remove("john")
#remove using del
del names[0]
#this is a range loop. It's different than the other array bellow.
for index in range(0,len(numbers)):
    print(f"index is {index} and value is {numbers[index]}")

#this finds specific things in the array 'names'    
for name in names:
    print(name)

def AskUserForInput():
    user_input = ipnut("Enter choice, press q to exit")
    return user_input
#use this bellow to use 'q' as the exit key or activation key
while AskUserForInput() != "q"
    print("do something!")

for index in range (0,len(names)):
    print(f"indez is {index} and value is {names[index]}")



