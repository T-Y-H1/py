# 猜数字
number = 37
guess = int(input('Enter an integer : '))
if number == guess:
    print('congratulations,you gussed it.')
elif guess < number :
    print('No ,it\'s a little higher than that.') 
else:
    print ('No, it is alittle lower than that')

print('done')