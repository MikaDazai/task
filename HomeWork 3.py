# Home Work 3 
# EX 1 
# def area_code(phone_number: str) -> str:
#     start = phone_number.find("(") + 1
#     end = phone_number.find(")")
#     return phone_number[start:end]
# print (area_code(("(555) 867-5309")))

# EX 2 


lst = ["apple", "banana", "flick", "cherry" , "flick" ]
lst = [bool(word.replace("flick", "")) for word in lst]
print(lst)  


# Ex 3 

def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))

santas_list = ["Fil","Stiv", "LIR", "Fenix"]
children = ["Fenix","Claudio", "Fil", "Stiv", "Lir"]   
print(find_children(santas_list, children))

