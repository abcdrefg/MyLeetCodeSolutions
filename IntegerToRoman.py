def intToRoman(num: int) -> str:
    sets = [('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M')]
    romanian_num = ''
    for i in range (1, 3):
        base, half, next_base = sets[i-1]
        howManyBase = num % 10
        if i == 2:
            howManyBase = num % 100
            howManyBase = howManyBase % 10
        if i == 3:
            howManyBase = num % 1000
            howManyBase = howManyBase % 100
            howManyBase = howManyBase % 10

        if howManyBase == 9:
            romanian_num = base + next_base + romanian_num
            continue
        if howManyBase > 5:
            for x in range(howManyBase):
                romanian_num = base + romanian_num
            romanian_num = half + romanian_num
            continue
        if howManyBase == 5:
            romanian_num = half + romanian_num
            continue
        if howManyBase == 4:
            romanian_num = base + half + romanian_num
            continue
        for x in range(howManyBase):
            romanian_num = base + romanian_num
    return romanian_num






print(intToRoman(190))