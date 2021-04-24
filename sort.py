import sys

number1 = int(sys.argv[1])
number2 = int(sys.argv[2])
number3 = int(sys.argv[3])
number4 = int(sys.argv[4])
number5 = int(sys.argv[5])

changes = 1
counter = 0
while changes > 0:
    changes = 0
    if number2 < number1:
        number1, number2 = number2, number1
        changes += 1
    if number3 < number2:
        number2, number3 = number3, number2
        changes += 1
    if number4 < number3:
        number3, number4 = number4, number3
        changes += 1
    if number5 < number4:
        number4, number5 = number5, number4
        changes += 1
    counter += 1
    print(f'In {counter}. iteration we had {changes} changes.')

print(f'Numbers from minimum to maximum are: {number1}, {number2}, {number3}, {number4}, {number5}.')


