def analyse_string(input_string):
    special_characters = 0
    analysis = {"special characters": 0, "words": 0, "total characters": 0}
    
    stripped_string = input_string.strip()
    total_characters = len(stripped_string)
    analysis.update({"total characters":total_characters})
    
    for character in range(total_characters):
        if set("(#$%&'()*+,-./:;<=>?@[\]^_`{|}~").intersection(stripped_string[character]):
            special_characters += 1
    analysis.update({"special characters":special_characters})
    
    stripped_sentance = input_string.strip("(#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    words = stripped_sentance.split()
    analysis.update({"words": len(words)})
    
    return analysis

string = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. spam=%seggs=%d % ("blah", 2) evaluates to spam=blah eggs=2'

print(f"Your string has {analyse_string(string)}.")