# CensorWords
# Instructions

# Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". The match is case-sensitive. Do not use import or regular expressions.
def censor_words(text, banned_word):
    return text.replace(banned_word, "***")