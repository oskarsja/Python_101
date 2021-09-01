# #2. lekcija (19.08.2021)
# ########################

# # 1. Uzdevums
# # Uzrakstiet programmu, kas noprasa un saglabā lietotāja vārdu
# username = input("What is your username?") 
# #print(username)

# # Uzdod jautājumu par lietotāja vecumu, jautājumā izmantojot lietotāja vārdu.
# age = input(f"{username}, what is your age?")
# #print(age)

# # Uzrāda pēc cik gadiem lietotājam būs 100 gadi :)
# import datetime 
# currentYear = datetime.datetime.now().year
# oldafter = str(+currentYear + 100 - int(age))

# print(f"{username} will be 100 years old at year: {oldafter}")


# # 2. Uzdevums
# # Uzdod 3 jautājums par telpas platumu, garumu, augstumu
# wide = input("how wide is the room?")
# long = input("how long is the room?")
# high = input("how high is the room?")

# # Uzrāda cik liels būs telpas tilpums
# volume = int(wide) * int(long) * int(high)
# print(f"Room volume is {volume}m3")


# # 3. Uzdevums - Celsijs uz Farenheitu
# # Uzrakstiet programmu, kas noprasa temperatūru pēc Celsija un izdrukā šo temperatūru pēc Farenheita skalas.
# celsium = input("what is the temperature in C?")
# farenheit = 32 + int(celsium) * (9 / 5)
# print(f"{celsium} degrees in C = {farenheit} degrees in F")








