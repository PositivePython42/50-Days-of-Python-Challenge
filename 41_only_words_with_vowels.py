def words_with_vowels(search_phrase):
    search_phrase.strip("'")
    words = search_phrase.split()
    vowel_words = []
    
    for word in words:
        if set('aeiouAEIOU').intersection(word):
            vowel_words.append(word)
    
    return vowel_words

input_phrase = input("Enter your phrase : ")
print(f"The words with vowels in from your phrase are {words_with_vowels(input_phrase)}.")

class Car:
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print(f"\ncar_model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")


bmw1 = Car("BMW x6", "silver", 2018, "Auto", False)
tesla1 = Car("Tesla S", "beige", 2017, "Auto", True)
ford1 = Car("Focus", "white", 2020, "Auto", False)

ford1.print_cars()