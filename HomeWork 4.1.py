# У даному випадку, весь код написано за Вас) Ваша ж задача прописати аннотації до функцій.


# ---=============---
def add(num1: int , num2:int ) -> int :  # Робимо функцію
    return num1 + num2  #Ставимо усову і закінчуемо 

print(add(5, 3))        
# ---=============---
old_list = ["apple", "pear", "banana"]    # Робимо list 

def add_element_to_list(lst: list , element : str ) -> list :    # Робимо функцію з (lst, element)
    lst.append(element)           #Додаємо в lst (element)
    return lst          # Закінцуемо функцію 

print(add_element_to_list(old_list, "grape"))          
# ---=============---
def multiple(num1: int , num2:int ) -> int :           # робимо функцію 
    return num1 * num2              # ставимо умову 

print(multiple(5.1, 3))              
# ---=============---
def create_list_of_random_numbers(length: int) -> list[int]:      
    import random
    lst = []                                
    for _ in range(length):                    
        lst.append(random.randint(0, 100))  
    return lst                               

print(create_list_of_random_numbers(10)) 
# ---=============---



