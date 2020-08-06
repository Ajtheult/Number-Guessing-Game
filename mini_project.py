# Asaph Franks Class 2

import random  # import's the random module
import datetime  # import's the datetime module

# User Details - start
userName = str(input("Please enter your name:"))  # user inputs name
userAge = int(input("Please enter your age:"))  # user inputs age
while userAge < 18:  # if the age as below 18 then the code exits
    print('You are too young. Get out of here.')
    exit()
Time = datetime.datetime.now()  # let the time and date show and assign a variable to it
print("---------------------------------")  # separates sections to keep the running product neat
# User list - start

user_list = []  # initialize user list
# try:
for i in range(0, 6):
    user_numbers = int(input("Enter a number between 1 and 49:"))  # gets user to input numbers between 1 and 49
    # except ValueError as i:
    #     print(i)
    if user_numbers < 1 or user_numbers > 49:
        user_numbers = int(input("Retry:Enter a number between 1 and 49:"))  # if the number and smaller than 1
    # and larger than 49 the person has to re-enter a number

    user_list.append(user_numbers)  # adds the numbers to the list

user_list.sort()  # sorts the numbers in ascending order

# User list - End

print("---------------------------------")  # separates sections to keep the running product neat

# Lotto Numbers - Start
lotto_num_list = []  # initialize lotto list

for i in range(0, 6):
    lotto_numbers = random.randint(1, 49)  # generates random numbers between 1 and 49 for lotto

    lotto_num_list.append(lotto_numbers)  # appends the random numbers to a list

lotto_num_list.sort()  # sorts the list in ascending order
# Lotto Numbers - End

# prints the lists out -start
print(userName, "'s numbers are: ")
print(user_list)

print("The 6 lotto numbers are: ")
print(lotto_num_list, "\n\n")
# prints the lists out -end


counter = 0  # set counter to 0
for user_numbers in user_list:
    if user_numbers in lotto_num_list:  # checks if there are similar numbers in both lists
        counter += 1  # if yes then add 1 to the counter

print("You have guessed " + str(counter) + " number(s) correctly")  # prints how many the user got right.

# if statement to determine what the prize is -start
if counter == 6:  # if the counter is 6 then the person wins R10,000 000.00
    print(userName, "has won R10,000 000.00")
elif counter == 5:  # if the counter is 5 then the person wins R8,584,00
    print(userName, "has won R8,584,00")
elif counter == 4:  # if the counter is 4 then the person wins R2,384.00
    print(userName, "has won R2,384.00")
elif counter == 3:  # if the counter is 3 then the person wins R100.50
    print(userName, "has won R100.50")
elif counter == 2:  # if the counter is 2 then the person wins R20.00
    print(userName, "has won R20.00")
else:  # if the counter is 1 or 0 then the person wins R0
    print(userName, "has won nothing")
# if statement to determine what the prize is -end

# everything that is going to written in the txt file - start
file = open("Mini_project.txt", "w")  # open file to write
# write all the details the user has inputted
file.write("-Name: \n")
file.write(userName + " \n")
file.write("-Age: \n")
file.write(str(userAge) + " years old" + "\n")
file.write("-Time:\n")
file.write(str(Time) + "\n")
file.write("-The numbers the user has entered\n")
file.write(str(user_list) + "\n")
file.write("-Prize:\n")
file.write("You have guessed " + str(counter) + " number(s) correctly\n")
# if statement to print the prize the user has won because a print statement won't work when writing to a file
if counter == 6:
    file.write("You have won R10,000 000.00")
elif counter == 5:
    file.write("You have won R8,584,00")
elif counter == 4:
    file.write("You have won R2,384.00")
elif counter == 3:
    file.write("You have won R100.50")
elif counter == 2:
    file.write("You have won R20.00")
else:
    file.write("You have won nothing")
file.close()  # closes the file.
# everything that is going to written in the txt file - close
