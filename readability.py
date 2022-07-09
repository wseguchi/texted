def readability(text):

    # calculates index according to Coleman-Liau method
    L = (count_letters(text) / count_words(text)) * 100
    S = (count_sentences(text) / count_words(text)) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # prints formated final result
    if index < 1:
        return("Before Grade 1")
    elif index >= 16:
        return("Grade 16+")
    else:
        return(f"Grade {index}")


def count_letters(text):
    num_letters = 0
    for i in range(len(text)):
        if text[i].isalpha():
            num_letters += 1
    return num_letters


def count_words(text):
    num_words = len(text.split())
    return num_words


def count_sentences(text):

    # count the number of ocorrences of [. , ! , ?] and counts as a sentence
    num_sentences = 0
    for i in range(len(text)):
        if text[i] in [".", "!", "?"]:
            num_sentences += 1
    if num_sentences == 0:
        num_sentences = 1
    return num_sentences