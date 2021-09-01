# 1) Uzģenerēt 1-100 un izdrukāt: Ja skaitlis dalās ar 5 tad 'Fizz'. Ja skaitlis dalās ar 7 tad 'Buzz'. Ja skaitlis dalās ar 5 un 7 tad 'FizzBuzz'. Savādāk pats skaitlis.
for i in range(1, 101):
        if i == 100:
            print(i, end = '\n')
        elif i % 5 == 0 and i % 7 == 0:
            print('FizzBuzz', end = ', ')
        elif i % 5 == 0:
            print('Fizz', end = ', ')
        elif i % 7 == 0:
            print('Buzz', end = ', ')
        else:
            print(i, end = ', ')
 
# 2) Ievadiet eglītes augstumu un izdrukājiet eglīti:
height = 3

for i in range(height):
    print(' ' * (height - i) + '*' * (2 * i + 1))

# Otrādāk
# for i in range(height, -1, -1):
#     print(' ' * (height - i) + '*' * (2 * i + 1))
 
# 3) Atrodiet vai ievadītais veselais pozitīvais skaitlis ir pirmskaitlis.
number = 6
 
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f'{number} is not a prime number because {i} * {number // i} = {number}')
            break
    else:
        print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')