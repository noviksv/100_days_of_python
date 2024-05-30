import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#read data from csv to dataframe
df = pd.read_csv("nato_phonetic_alphabet.csv")
#convert dataframe to dictionary
data = df.to_dict()

# print(data)
nato_alphabet = {v.letter:v.code for (k,v) in df.iterrows()}

print(nato_alphabet)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    
    word = input("Enter a word: ").upper()
    try:
        word_list = [nato_alphabet[i] for i in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(word_list)

generate_phonetic()
