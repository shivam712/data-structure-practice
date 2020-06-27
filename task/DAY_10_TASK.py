def recursive_multiply(x, y):
    if y!=0:
        return x + recursive_multiply(x,y-1)
    else:
        return 0
print(recursive_multiply(25,10))

vowels=['a','i','e','o','u']
def recursive_count_consonants(string):
    if string == '':
        return 0

    if string[0].lower() not in vowels and string[0].isalpha():
        return 1 + recursive_count_consonants(string[1:])
    else:
        return recursive_count_consonants(string[1:])
print(recursive_count_consonants('shivam'))