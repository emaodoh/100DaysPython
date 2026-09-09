# CensorWords
# Instructions

# Implement censor_words(text, banned_word). Return a new string where every occurrence of banned_word is replaced with "***". The match is case-sensitive. Do not use import or regular expressions.

def censor_words(text, banned_word):
    text = text.split()


    result = ""

    for word in text:
        
        if word == banned_word:
            result += "***"
            result += " "
            
        else:
            result += word
            result += " "
    return result


result  = censor_words("my name is john i am 29 years", "john")

print(result)
