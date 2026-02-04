# program that takes a list of strings, filters out strings shorter than 4 characters,
#  and converts the remaining strings to uppercase
# given input= ["apple", "bat", "car", "dolphin", "egg", "fish"]
# expected output= ["APPLE", "DOLPHIN", "FISH"]


words= ["apple", "bat", "car", "dolphin", "egg", "fish"]

filtered_words= [w.upper() for w in words if len(w) >=4]
print(filtered_words)  # Output: ['APPLE', 'DOLPHIN', 'FISH']

