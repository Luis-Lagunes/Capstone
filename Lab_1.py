
name = input('What is your name? ')
letters = len(name)
birthMonth = input('What month were you born in? ')

print('Hello ' + name + ' nice to meet you!')
print('Did you know that there are ' + str(letters) + ' letters in your first name?')

if birthMonth == 'September':
    print('Happy Birthday ' + name + '!')
else:
    print('Nice,' + birthMonth + ' is a great month!')

classes = [] # creates an empty list

count = int(input('How many classes are you taking this semester? ')) # counts the entered number
for i in range(count): # creates a loop that keeps going until it reaches the entered number
    class_names = input('Enter the name of class ' + str(i + 1) + ': ')
    classes.append(class_names)

print('Your classes are:', classes)