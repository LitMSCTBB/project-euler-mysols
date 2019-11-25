# Problem 17
# Number Letter Counts
# stolen from Bill9000 on AOPS



# Huh. Looks very confusing.
# Also, are they British? Hm.
# I don't like this one because it doesn't deal purely with maths. (haha maths)

def letters(n):
    '''
    letters(n) -> int
    Returns the number of letters in n when written out in English.
    '''
    # Extreme exception.
    if n == 1000:
        return 11
    
    letterCount = 0
    
    # CASES!
    units = int(str(n)[-1])
    tens = 0
    hundreds = 0
    if n >= 10:
        tens = int(str(n)[-2])
    if n >= 100:
        hundreds = int(str(n)[-3])
    
    # Ok, up units. (0 doesn't count.)
    if tens != 1:
        if units in [1, 2, 6]:
            letterCount += 3
        elif units in [4, 5, 9]:
            letterCount += 4
        elif units in [3, 7, 8]:
            letterCount += 5

    # Add up tens.
    
    # TEENS FIRST!
    if tens == 1:
        teens = n % 100
        if teens in [10]:
            letterCount += 3
        elif teens in [11, 12]:
            letterCount += 6
        elif teens in [15, 16]:
            letterCount += 7
        elif teens in [13, 14, 18, 19]:
            letterCount += 8
        elif teens in [17]:
            letterCount += 9
    else:
        if tens in [4, 5, 6]:
            letterCount += 5
        elif tens in [2, 3, 8, 9]:
            letterCount += 6
        elif tens in [7]:
            letterCount += 7

    # Add up hundreds.
    if hundreds in [1, 2, 6]:
        letterCount += 10
    elif hundreds in [4, 5, 9]:
        letterCount += 11
    elif hundreds in [3, 7, 8]:
        letterCount += 12

    # Um...OH! The 'and'.
    if hundreds > 0 and units + tens > 0:
        letterCount += 3

    # Ok, return.
    return letterCount

def blah():
    '''
    blah()
    Whatever.
    '''
    # Let's test this.
    import random
    for i in range(10):
        n = random.randrange(1, 1001)
        print(str(n) + ' has ' + str(letters(n)) + ' letters.')
        print()
        

# LET'S DO THIS!
runningTotal = 0

for i in range(1, 1001):
    runningTotal += letters(i)

# DONEEEEEE!!!!
print(runningTotal)