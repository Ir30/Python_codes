import string
def sort_and_pricess_the_string(input_string):
    
    alphabet_loewr = string.ascii_lowercase
    alphabet_lower = list(alphabet_loewr)
    # print(alphabet_list)

    lower_dict={x:y for x,y in zip(alphabet_loewr,[i for i in range(1,27)])}
    # print(lower_dict)
    
    alphabet_upper = string.ascii_uppercase
    alphabet_upper = list(alphabet_upper)
    # print(alphabet_upper)
    upper_dict={x:y for x,y in zip(alphabet_upper,[i for i in range(27,53)])}
    # print(upper_dict)
    
    string_list=input_string.split(" ")
    def find_weight_and_swap(s):
        weight=0
        swaped=''
        for i in s:
            if i.isupper() == True:
                weight+=upper_dict[i]
                swaped += i.lower()
            else:
                weight+=lower_dict[i]
                swaped+=i.upper()
        
        return weight,swaped
    
    weighted_dict={}
    
    for i in string_list:
        weight,swaped=find_weight_and_swap(i)
        weighted_dict[weight] = swaped
        
    # print(weighted_dict)
    sorted_weight=sorted(list(weighted_dict.keys()),reverse=True)
    # print(sorted_weight)
    out = ''
    for i in sorted_weight:
        out+=" "+weighted_dict[i]
    
    return out

print(sort_and_pricess_the_string("aBC DeF"))