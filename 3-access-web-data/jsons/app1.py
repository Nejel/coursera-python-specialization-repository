import json

data = json.load(open('data.json')) #open json with dictionary

def translate(w):
    w = w.lower() #make it lowercase to prevent errors
    if w in data:
        return data[w]
    else:
        return "Nope, that's not working"

word = input("Enter word: ")
print(translate(word))
