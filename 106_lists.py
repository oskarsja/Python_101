# 1.a Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float). Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus. Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
try:
    list = []
    while True:
        numbers = input('\nPress "q" to quit. \nEnter any number to continue: ')
        if 'q' in numbers:
            print('Successfuly QUIT.\n')
            break
        else:
            numbers = float(numbers)
            list.append(numbers)
            print(f'\nList of all numbers: {list}')
            list.sort()
            print(f'BOTTOM 3: {list[0:3]}')
            print(f'TOP 3: {list[-3:len(list)]}')
            print(f'Average: {round(sum(list) / len(list), 2)}\n')
except Exception as e: 
    print(f'Error: {e}\n')
 
# 2. Lietotājs ievada sākumu un beigu skaitli. Izvads ir ievadītie skaitļi un to kubi.
# Piemērs: ievads 2 un 5. Izvade:
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
list = []
start = int(input('Input starting number: '))
end = int(input('Input starting number: '))
for i in range(start, end + 1):
    print(f'{i} kubā: {i * i *i}')
    list.append(i * i * i)
print(f'Visi kubi: {list}')
 
# 3. Lietotājs ievada teikumu. Izvadam visus teikuma vārdus apgrieztā formā. Var noderēt split un join operācijas.
# Piemērs: Alus kauss -> Sula ssuak
sentence = input('Enter a sentence: ').lower().split()
reverse_words = [sentence[::-1] for sentence in sentence]
reverse_sentence = " ".join(reverse_words).capitalize()
print(reverse_sentence)
  
# 4. Pirmskaitļi. Atrodiet un izvadiet pirmos N pirmskaitļus saraksta veidā.
# Piemērs: [2,3,5,7,11,...]
prime_list = []
n = int(input('Input number of prime numbers you want to see: '))
i = 1
count = 0
 
while (count < n):
    for x in range(i, i + 1):
        c = 0
        for y in range(1, x + 1):
            if (x % y == 0):
                c += 1
        if (c == 2):
            count += 1
            prime_list.append(x)
    i += 1
print(prime_list)