import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
alpha_dict = {row.letter:row.code for (index,row) in df.iterrows()}
word = input('Type a word:').strip().replace(" ","")
try:
    letters = [alpha_dict[letter.upper()] for letter in word]
except KeyError:
    print("please write only letters without special characters")
print(f" Coded Word: {letters}")