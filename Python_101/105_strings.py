# # 1) Lietotājs ievada vārdu. Tiek atgriezts lietotāja vārds apgriezts un sākas ar lielo burtu un papildu tekstu "pamatīgs juceklis vai ne pirmais lietotāja burts?"
# Piemērs: Oskars -> Srakso, pamatigs juceklis vai ne O?
name = input('Input your name: ')
#name = 'Oskars'
name_first_letter = name[0]
reverse_name = name.lower()[::-1]
print(f'{reverse_name.capitalize()}, pamatigs juceklis vai ne {name_first_letter.upper()}?')
 
# # Uzrakstīt programmu teksta simbola atpazīšanai
# # Lietotājs (pirmais spēlētājs) ievada tekstu.
# # Tiek izvadītas tikai zvaigznītes burtu vietā (atstarpe nav ar zvaigznīti un ciparu nav)
# # Lietotājs (otrs spēlētājs) ievada simbolu. 
# # Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# # Piemērs: Kartupeļu lauks -> ********* *****. Pēc ievades: a -> *a****** *a***
 
text_input = input('Enter word combination for guessing game: ') 
word = hidden_word = text_input.lower()
for i in range(len(hidden_word)):
    hidden_word = hidden_word[0:i] + "*"
    if ' ' in word:
        hidden_word = hidden_word[:word.index(' ')] + ' ' + hidden_word[word.index(' ')+1:]
print(hidden_word) 
 
while hidden_word != word:
    guess = input("Enter a single letter: ")
    guess = guess.lower()
    for i in range(len(word)):
        if word[i] == guess:
            hidden_word = hidden_word[0:i] + guess + hidden_word[i + 1:]
    print(hidden_word) 
print(f"You have guessed '{word}' correclty.")
 
# Uzrakstīt programmu teksta pārveidošanai
# Saglabā lietotāja ievadu un izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Piemēri: Laiks nav slikts -> Laiks ir labs / Auto nav jauns -> Auto nav jauns / Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs 
# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba
 
option1 = '\n1. Laiks nav slikts'
option2 = '\n2. Auto nav jauns'
option3 = '\n3. Tas biezpiens nav nemaz tik slikts'
option4 = '\n\n4. Gribu ievadīt pats savu tekstu'
 
print('Choose a text to modify (1 - 4):', option1, option2, option3, option4)
 
choice = int(input('\nSelect a number from list above: \n'))
 
if choice == 1:
    print('\nChosen text: ' + option1[4:])
    original_text = option1[4:]
elif choice == 2:
    print('\nChosen text: ' + option2[4:])
    original_text = option2[4:]
elif choice == 3:
    print('\nChosen text: ' + option3[4:])
    original_text = option3[4:]
elif choice == 4:
    choice = input('Enter your text: ')
    print('\nChosen text: ' + choice)
    original_text = choice
else:
    original_text = 'Only numbers 1 through 4 are accepted. Restart the application.'
 
# #original_text = input('Input your negative text here: ')
text = original_text.split(' ')
starting_word = 'nav'
ending_word = 'slikt'
starting_word_replacement = 'ir'
ending_word_replacement = 'lab'
order = original_text.find(ending_word)
 
if starting_word in original_text and ending_word in original_text and text.index(starting_word) < text.index(ending_word + original_text[order + len(ending_word)]):
    text_before_starting_word = original_text.split(starting_word)[0]
    text_after_ending_word = original_text.split(ending_word)[1]
    print('Modified text: ' + text_before_starting_word + starting_word_replacement + ' ' + ending_word_replacement + text_after_ending_word)
else:
    if original_text != 'Only numbers 1 through 4 are accepted. Restart the application.':
        print('Nothing to fix here')
    else:
        print(original_text)


# https://pastebin.com/59MfvHi2





# alterinatīvais variants 2. uzdevumam
# hidden_word = ""
# for c in word:
#     if c == " ":
#         hidden_word += c 
#     else:
#         hidden_word += "*"

# tries = 0
# max_ties = 7
# while hidden_word != word:
#     guess = input("Enter a single letter: ")
#     guess = guess.lower()
#     temp_word = ""
#     for c, guess_char in zip(word, hidden_word): #two strings at once
#         if c == guess_char or c == guess: #we check for id gues sor new guess both are good
#             temp_word += c 
#         else:
#             temp_word += "*"
#     hidden_word = temp_word
#     print(f'your guess so far: {hidden_word}')
#     tries +-1
#     if tries >= max_ties:
#         print("you lost!")
#         break