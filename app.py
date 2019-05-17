import json
from difflib import get_close_matches

data = json.load(open('dictionary_app/data.json'))


def finding_word_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? \n Enter Y for yes and N for no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "OK"
            pass
        else:
            return "We did not understand your entry."
    else:
        return "The word does not exist, please re-type."


user_input = input("Write a word, which I should look for: ")

output = finding_word_definition(user_input)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)