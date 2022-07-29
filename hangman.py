
#print(guessed_word_list)
#print("Das gesuchte Wort ist " + str(length), "Zeichen lang.")
#guess1 = input("Rate einen Buchstaben, der deiner Meinung nach im gesuchten Wort enthalten ist: ")

word_to_guess = "HELLO"
length = len(word_to_guess)
guessed_word_list = []
xxx = ["*","*","*","*","*"]


def compare_lists(list1, list2):              #feststellen wann eingegebene Buchstaben == gesuchtem Wort --> OK
    if sorted(list(list1)) == sorted(list(list2)):
        return "equal"
    else:
        return "non equal"


def check_word(guess1):   #Vergleich des eingegebenen Buchstabens mit jedem Buchstaben aus dem gesuchten Wort --> OK
    for char in word_to_guess:
        if guess1 != char:
            print("-")
        if guess1 == char:
            i = 0
            print(guess1)
            guessed_word_list.append(char)
            xxx[i] = guess1
            i += 1


def checked_words(guessed_word_list, word_to_guess):    #Speichern der gefundenen Buchstaben --> leerer Output
    for char in word_to_guess:
        if char == word_to_guess:
            print(char)
        else:
            print("-")



while compare_lists(guessed_word_list, word_to_guess) == "non equal":
    print(xxx)
    print("*****")
    #checked_words(guessed_word_list, word_to_guess)
    check_word(input("Rate einen Buchstaben, der deiner Meinung nach im gesuchten Wort enthalten ist: "))

if compare_lists(guessed_word_list, word_to_guess) == "equal":
    print("*****")
    print("Gewonnen, das gesuchte Wort lautete " +word_to_guess)
    print("*****")
