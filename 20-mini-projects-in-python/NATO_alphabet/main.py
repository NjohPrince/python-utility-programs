import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Alternatively,
# letters = data.letter.to_list()
# codes = data.code.to_list()
# phonetic_dict = {key: value for (key, value) in zip(letters, codes)}

while True:
    word = input("Enter a word to encode or 'quit' to exit: ").upper()
    if word == "QUIT":
        break
    if word.isalpha():
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
