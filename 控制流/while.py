number = 37
running = True

while running:
    guess = int(input("Enter a number."))
    if guess == number:
        print('congratulations,you gussed it.')
        running = False
    elif guess < number :
        print('No ,it is a little higher than that.') 
    else:
        print ('No, it is alittle lower than that')
else:
	    print('The loop is over.')

print('Done')