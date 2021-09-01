# import math

# #1. Uzrakstiet programmu, kas pārbauda lietotāja temperatūru
# # < 35 = "nav par aukstu"
# # 35 - 37 (ieskaitot) = "viss kārtībā"
# # > 37 = "iespējams drudzis"

# temperature = float(input("Kāda ir Tava teperatūra?"))

# if temperature < 35:
#     print("nav par aukstu")
# elif temperature > 37:
#     print("iespējams drudzis")
# else:
#     print("viss kārtībā")    


# #  2. Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem
# # Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu
# # Izvadiet bonusu

# salary = float(input("Kāda ir Tava alga?"))
# experience = float(input("Kāds ir Tavs darba stāžs?"))

# if math.floor(experience) > 2:
#     print((math.floor(experience) - 2) * salary / 100 * 15)
# else:
#     print(0)


# # 3. Noprasiet lietotājam ievadīt 3 skaitļus, izvadiet tos sakārtotā secībā.
# # Uzdevumu risinam tikai ar if, elif, else darbībām
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

# if a > b:
#     a,b = b,a
# if a > c:
#     a,c = c,a
# if b > c:
#     b,c = c,b
    
# print (a, b, c)
