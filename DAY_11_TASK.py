def is_unique(str): 
    for i in range(len(str)): 
        for j in range(i + 1,len(str)):  
            if(str[i] == str[j]): 
                return False; 
    return True

def str_to_int(input_str):
    result = 0
    for digit in input_str:
        result *= 10
        for d in '0123456789':
            result += digit > d
    return result
print(str_to_int('132424'))
