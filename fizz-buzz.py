
for x in range(1,25):
    seb = ''

    if x % 3 == 0:
        seb += 'fizz'

    if x % 5 == 0:
        seb += 'buzz'

    if seb == '':
        seb = str(x)

    print(seb)
