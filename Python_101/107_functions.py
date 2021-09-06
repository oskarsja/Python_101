# 1. Uzrakstiet funkciju add_mult, ar trīs parametriem. Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# Piemērs: add_mult(2,5,4) -> atgriezīs 30
def add_mult(number1, number2, number3):
    my_list = [number1, number2, number3]
    my_list.sort()
    bottom = sum(my_list[0:2])
    top = my_list[-1]
    result = bottom * top
    return(result)

print(add_mult(2,5,4))

# 2. Uzrakstiet funkciju is_palindrome(text), kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# Piemērs: is_palindrome("Alus ari ira      sula") -> True
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    reverse_text = text.lower()[::-1]    
    result = text == reverse_text
    return(result)

print(is_palindrome('Alus ari ira      sula'))

# 3. Pilsēta
# Pilsētā ir zināms skaits iedzīvotāju p0
# Katru gadu nāk klāt procentuāls skaits perc
# Katru gadu nāk klāt(vai aizbrauc) arī zināms skaits delta
# Mums ir jāzina, kad(ja vispār) pilsēta sasniegs iedzīvotāju skaitu p
# Uzrakstiet funkciju get_city_year(p0, perc, delta, p) kas atgriež gadus (pilnus) kad p tiks sasniegts.
# Ja p nevar sasniegt, tad atgriežam -1
# Piemērs: get_city_year(1000,2,50,1200) -> 3
# 1000 + 1000 * 0.02 + 50 => 1070 pēc 1.gada
# 1070 + 1070 * 0.02 + 50 => 1141 pēc 2.gada
# 1141 + 1141 * 0.02 + 50 => 1213 pēc 3.gada
# PS. Ievērojam, ka padodam perc kā procentu kas jāpārvērš decimāl skaitlī.
# Pārbaudam, vai strādā ar sekojošiem parametriem:
# get_city_year(1000, 2, -50, 5000) -> -1 # samērā aktuāla problēma
# get_city_year(1500, 5, 100, 5000) -> 15
# get_city_year(1500000, 2.5, 10000, 2000000) -> 10
def get_city_year(p0, perc, delta, p):
    count = 1
    perc = perc / 100
    formula = p0 + p0 * perc + delta
    if formula > p0:
        while p0 < p:
            p0 = p0 + p0 * perc + delta
            if p0 >= p:
                break
            else:
                count += 1
    else:
        count = -1
    return(count)

print(get_city_year(1000,2,50,1200))