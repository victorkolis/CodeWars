# Link: https://www.codewars.com/kata/5713bc89c82eff33c60009f7

def to_freud(sentence):
    return sentence if sentence == '' else f'{(sentence.count(" ") + 1) * "sex "}'.strip()


print(to_freud("I love sex"))
