# # ЦЫКЛЫ   
# number = 3
# list_1 = [1, 2, 3, 3, 2 ,5 ,6 ]
# print(list_1.count(number))


# lst  =[1, 2, 3, 4, 5 ]
# print (len(lst))               # 5 
# print (lst[0:3])               #[1, 2, 3 ]
# print (lst[3:])                 #[4, 5]
# print (lst[1:5:2])            # [2,4]
# print (lst[::-1])               # [5 , 4, 3, 2 ,1  ]
# print (lst[1:5:-1])           # []
# print (lst[::-2])               # [4, 2   ]
# res = lst[::-1]
# print (res)


link = "https://www.google.com/get_the_data/12340"
link1 = link.split("/")
print (link1)
print (link1[3])


# fruit = "apple"
# for i in range (len(fruit)):
#     print (fruit [i]) 

# fruit_1 = 130492039
# str_fruit_1 = str(fruit_1)
# reselad_list = []

# for num in range(0 , len (str_fruit_1)):
#     reselad_list.append(int (str_fruit_1[num]))
    
# print (sum(reselad_list))


# lst_v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# for fruit in range (0 , len(lst_v)):
#     print (lst_v[fruit]) 

# lst_1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# lst_2 = ["cherry", "orange", "carrot", "cucumber", "tomato", "pepper" , "melon" , "mango"]

# # resuld = []
# # for fruit in lst_2: 
# #     if fruit not in lst_1:
# #         lst_1.append(fruit)
# # print (lst_1)
# set_list = set(lst_1 + lst_2)
# # print (set_list)
# # list_list = list (set(set_list))
# dick_list  = sorted(set_list , reverse = True)

# print (dick_list) 
 
n_num = [1, 2 ,3 , 4 ]
p_num = [-1 , -2 , -3 , -4]
# sum_p_num = sum (p_num)
# sum_n_num = sum (n_num)

# print ([sum_n_num  , sum_p_num])
# result = [0,  -0]
# for num1 in p_num:
#     result[0] += num1
# for num2 in n_num:
#     result[1] += num2
# print (result )
print (sum(p_num ) , sum (n_num))