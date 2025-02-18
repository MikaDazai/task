lst1  = [1 , 2 , 3 , 4 ]
lst2 = [4 , 5 , 6 ] 
not_more = 4


def get_unqiue_numbers(lst1: list, lst2: list)  -> list:
    sum_lst = lst1 + lst2
    set_lst = list (set(sum_lst))
    return  set_lst
print(get_unqiue_numbers(lst1, lst2))

def sum_lower_than(lst1:list , lst2:list , not_more: int ) -> list :
    result = []
    for i in get_unqiue_numbers(lst1, lst2):
        if i <= not_more:
            result.append(i)
    return result

print(sum_lower_than(lst1, lst2, not_more ))


# def get_unqiue_numbers(lst1, lst2):
#     lst1 += [num for num in lst2 if num not in lst1]
#     return lst1

# print(get_unqiue_numbers(lst1, lst2))

# def sum_lower_than(lst1, lst2, not_more):
#     return [num for num in get_unqiue_numbers(lst1, lst2) if num <= not_more]

# print(sum_lower_than(lst1, lst2, 3))