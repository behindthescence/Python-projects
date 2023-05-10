#My first python practice project asking for user name and number from 1 to 3 to select his/her favourite fruit.   

#Declering Variables
User_name = input('Please enter your name: ')
User_numb = int(input( "Please enter a number from (1 to 3) to select your favorite fruit: "))
fruits = ['Orange', 'Apple', 'Cherry', 'Banana']

#Setting conditions for user's name
if User_name != "":
    print('Hello', User_name)

else:
    print('Please enter your fucking name mehn!')

#Setting conditions for user's selected number
if User_numb == 3:
    print('Your favorite fruit is', fruits[0])

if User_numb < 3 != 1:
        print('Your favorite fruit is', fruits[1])

elif User_numb == 1:
    print('Your favorite fruit is' , fruits[2])
else:
    print('Please select from 1 to 3')