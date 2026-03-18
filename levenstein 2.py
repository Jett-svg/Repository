from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
print(a)

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, привет мир')
print(a)

