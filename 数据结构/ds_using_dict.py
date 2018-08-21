ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'larry':'larry@wall.com',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmaol.com'
}

print("Swaroop's address is ",ab['Swaroop'])

del ab['Spammer']

print('\nThere are {} contacts in the adress-bool\n',format(len(ab)))

for name,address in ab.items():
    print('contact {} at {}'.format(name,address))

ab['Guido'] = 'guido@python.org'

if 'guido' in ab:
    print("\nGuido's adress is",ab['Guido'])
else:
    print("No,cannot find it")