# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favoriteColor = input('Enter favorite color: \n')
favoritePet = input('Enter pet\'s name: \n')
userNum = int(input('Enter a number: \n'))
print('You entered:',favoriteColor, favoritePet, userNum)

# my changes here


# FIXME (2): Output two password options
password1 = favoriteColor + '_' + favoritePet
password2 = str(userNum) + favoriteColor + str(userNum)
print('\nFirst password:', password1)
print('Second password:', password2)


# FIXME (3): Output the length of the two password options
password1Len = len(password1)
password2Len = len(password2)
print('\nNumber of characters in %s: %d' % (password1,password1Len))
print('\nNumber of characters in %s: %d' % (password2,password2Len))
