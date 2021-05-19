import random

lower = str(input('Masukan huruf kecil : '))
upper = str(input('Masukan huruf besar : '))
number = str(input('Masukan Angka : '))
symbol = str(input('Masukan Symbol : '))

all = lower + upper + number + symbol
length = 16
password = "".join(random.sample(all, length))
password_width = len(password)
print(password)
