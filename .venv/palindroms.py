phrases = [
           "нажал кабан на баклажан",
           "дом как комод",
           "рвал дед лавр",
           "азот калий и лактоза",
           "а собака боса",
           "тонет енот",
           "карман мрак",
           "пуст суп"
]

def solve(phrases):
    result = []
    for phrase in phrases:
        phrase_new = phrase.replace(' ','') # сохраним фразу без пробелов
        if  phrase_new == phrase_new[::-1]: # сравним фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result