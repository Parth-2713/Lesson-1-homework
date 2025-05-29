#Make a dictionary of the capitals of the countries of the world
#and do the above operations on the worldCapitalDictionary.

worldCapitalDictionary = {
    'America' : 'Washington D.C.',
    'India' : 'New Delhi',
    'Canada' : 'Ottawa',
    'Mexico' : 'Mexico City'
}

print (worldCapitalDictionary['America'])
worldCapitalDictionary['Canada'] = 'Montreal'
worldCapitalDictionary['South Korea'] = 'Seoul'
del worldCapitalDictionary['Canada']
if 'America' in worldCapitalDictionary:
    print ('Yes')
else:
    print ('No')
for key in worldCapitalDictionary:
    print(key)
for value in worldCapitalDictionary.values():
    print(value)
print(len(worldCapitalDictionary))

#Write a program that uses a dictionary that contains ten usernames and passwords.
#The program should ask the user to enter their username and password.
#If the username is not in the dictionary,
#the program should indicate that the person is not a valid user of the system.
#If the username is in the dictionary, but the user does not enter the right password,
#the program should say that the password is invalid.
#If the password is correct,
#then the program should tell the user that they are now logged in to the system.

usernames_and_passwords = {
    'Parth' : 2013,
    'Percy_Jackson' : 2005,
    'Harry_Potter' : 1997,
    'Dad' : 1234,
    'Mom' : 5678,
    'Code' : 000,
    'Vanya' : 2023,
    'Art' : 1,
    'Math' : 0,
    'Winter' : 10
}

#Write a Python program to:
#Take input from the user for the following details:
#Name
#Age
#City
#Store them in a dictionary.
#Print the dictionary.
#Based on the dictionary you created in Question 3:
#Update the City to a new value entered by the user.
#Print the updated dictionary.

name = input('What is your name?')
age = int(input('What is your age'))
city = input('In which city do you live in?')

info = {
    name : [age,city]
}

print(info)

city2 = input('In which city do you live in now?')

info[city] = city2
print(info)