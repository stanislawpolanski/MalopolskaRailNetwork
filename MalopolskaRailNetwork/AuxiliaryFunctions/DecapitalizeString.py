def DecapitalizeString(input):
    splitted = input.split()

    result = None

    for word in splitted:
        word = word.lower()
        word = word.capitalize()

        if result is None:
            result = word
            continue

        result += " " + word
    return result
