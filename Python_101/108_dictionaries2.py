# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# Piemērs: get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} # vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut
# 1b. Uzrakstīt funkciju: get_digit_dict(num), kas saņem veselu skaitli kā parametru
# funkcija izvada ciparu izmantojumu skaitlī vārdnīcas formā
# Piemērs: Ievada 599637003 -> {'0':2, '1':0,....'7'':1,'8':0,'9':2} # rādam visiem cipariem izmantojamību
# PS 1a un 1b var atrisināt ar vienu un to pašu funkciju 1b vajadzībām nedaudz pielāgojot 1a kodu.
from collections import Counter

def get_char_count(text):
    if type(text) == int:
        numbers = '0123456789' #kā šo uzģenerēt?: str(dictionary)[int] = 0; Vai vispār nepieciešams to darīt?
        numbers = dict(Counter(str(numbers)))
        for n in numbers:
            numbers[n] = 0
        
        result = dict(Counter(str(text)))
        for sub in numbers:
            if sub in result:
                numbers[sub] = result[sub]
        return numbers
    else: 
        result = dict(Counter(str(text)))
        return result
    
print(get_char_count('hubba bubba'))
print(get_char_count(599637003))

# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
# Piemērs: clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10}, jo 5 bija vērtība, kas jānomaina.
def replace_dict_value(d, bad_val, good_val):
    clean_dict_value = d[0] #jāmeklē visas dict un jāapstrādā visas d?
    for key, value in clean_dict_value.items():
        if value == bad_val:
            clean_dict_value[key] = good_val
    return clean_dict_value

print(replace_dict_value(({'a':5,'b':6,'c':5}, 5, 10),5,10))

# 3.a Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# Piemērs: clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
def clean_dict_value(d, bad_val):
    clean_dict_value = d[0]
    new_dict = {}
    for key, value in clean_dict_value.items():
        if value != bad_val:
            new_dict[key] = value           
    clean_dict_value = new_dict
    return clean_dict_value

print(clean_dict_value(({'a':5,'b':6,'c':5}, 5), 5))

# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.
# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!
# Divi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu.
def clean_dict_values(d, v_list):
    delete = []
    for key, value in d.items():
        if value in v_list:
            delete.append(key)
            
    for i in delete:
        del d[i]
    return d

print(clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]))
