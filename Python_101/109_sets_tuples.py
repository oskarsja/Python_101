# 1. Min, Avg, Max
# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
# 1b tiem, kas pieredzējušāki
# Uzrakstiet funkciju get_min_med_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, medianu un lielāko vērtību no virknes.
# Median vērtība ir vērtiba, kas sakartotā virknē ir paša vidū. Ja virknes skaits ir pāra tad vidū ir divas vērtības.
# No vidus vērtībām tad ņem vidējo.
# get_min_med_max([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max("baaac") -> ('a','a','c')
#  # ar string var būt interesanti rezultāti pie pāra skaita ņemot vidējo, tāpēc labak dot abus vidējos
# get_min_med_max("faaacb") -> ('a', 'ab', 'f') 
# ienākošā sequence var būt tuple vai list ar vienāda tipa vērtībām, vai pat string.


# Uzrakstiet funkciju, kas spēj apstrādat patvalīgu skaitu virkņu un atgriež tuple ar kopējiem elementiem trijās virknēs. Virknes var būt list, tuple, string.
# get_common_elements("abc",['a','b'],('b','c')) -> ('b',) # tuple are vienu element šim elementam seko komats
def get_common_elements(*args):
    return tuple(set.intersection(*map(set, args)))

print(get_common_elements("abc",['a','b'],('b','c')))

# 3. Vai ir pangramma?
# Uzrakstīt funkciju is_pangram, kas atgriež True, kad mytext parametrs satur visus burtus kas padoti a alfabetā. Savadāk atgriežam False.
# Pangramma - teikums,vārdu virkne, kas satur visus alfabeta burtus.
# Atstarpes ignorējam, un uzskatam ka lielais burts ir tikpat derīgs kā mazais.
# def is_pangram(mytext, a = 'abcdefghijklmnopqrstuvwxyz'):
#     return str(mytext.lower()) >= a

# print(is_pangram('abcd foo'))
# print(is_pangram('The quick brown fox jumps over the lazy dog'))
# print(is_pangram('The five boxing wizards jump quickly'))

# #labāks veids:
# import string

# def ispangram(mytext):
#     a = set(string.ascii_lowercase)
#     return set(mytext.lower()) >= a

# print(ispangram('abcd foo'))
# print(ispangram('The quick brown fox jumps over the lazy dog'))
# print(ispangram('The five boxing wizards jump quickly'))