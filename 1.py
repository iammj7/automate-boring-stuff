#  this program says hello and asks for my name.
# i'm printing hello world
print("Hello, world!")
# i'm printing what's your name
print("what's your name ?")  # ask for their name
#  i'm taking input and assigning it to var
myName = input()
# i'm printing a string along my previous var
print("It is good to meet you, " + myName)
print("The length of your name is:")
# print a var length using len function
print(len(myName))
print('what is your age?')
#  by default all inputs will be stored as string
myAge = input()
# the below will print a blank line.
print()
#  printing string and concate converting str to int and add 1
print('You will be ' + str(int(myAge) + 1) + ' in a year')
