# determines if two strings are anagrams, contains the exact same characters 
# in a differet order

# word1= "listen", word2= "silent"

def is_anagram(str1, str2):

    s1= sorted(str1.lower().replace(" ", ""))
    s2= sorted(str2.lower().replace(" ", ""))

    print(s1, s2)
    return s1==s2


result= is_anagram("LISTEN", "SIlent")
print(result)