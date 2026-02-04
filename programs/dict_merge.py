# function that merge two dictionaries. If a key exists in both dictionaries, sum their values. 
# If a key exists in only one, include it as it is.

# given input: dict_a= {'a': 2, 'b': 3, 'c': 5}, dict_b= {'b': 4, 'c': 1, 'd': 7}
# expected Output: {'a': 2, 'b': 7, 'c': 6, 'd': 7}

def merge_dicts(d1, d2):
    result= d1.copy()

    for key, value in d2.items():
        print(key, value)
        # this line checks if the key exists in result, if not it uses 0 as default
        result[key]= result.get(key, 0) + value
        # breakpoint()

    return result




d1= {'a': 2, 'b': 3, 'c': 5}
d2= {'b': 4, 'c': 1, 'd': 7}
merged= merge_dicts(d1, d2)
print(merged) 