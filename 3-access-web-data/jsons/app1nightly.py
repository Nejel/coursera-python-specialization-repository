# check similarities with difflib and get_close_matches: https://www.udemy.com/the-python-mega-course/learn/v4/t/lecture/7627942?start=15

import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes and N if no: " % get_close_matches(w, data.keys())[0]) #first element of closest match
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "Nope, that's not working"

word = input("Enter word: ")
printed = translate(word)

#чтобы определения были на двух разых строчках
if type(printed) == list:
    for i in printed:
        print(i)
else:
    print(printed)
