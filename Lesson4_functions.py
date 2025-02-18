# def main (num1 , num2 ):
#     return num1 + num2
# print (main(2, 3 ))


# def Hello (name:str , age: int ) -> str:
#     return f"Hello {name}. Your compani {age} years old "

# print (Hello(name = " Misha " , age = 1212))
# num = 0 
# # while True:
# #     if num +  9 > 100:
# #         break 
# #     num += 9 
# #     print (num )



# while num < 108 :
#     num += 9 
#     print (num)

Url_links = [
"https://github.com/MikaDazai/task/blob/master/HomeW.py", 
"https://www.youtube.com/ofk/eopk"]
result = [ ]



def get_n_f_s_l (url: list ) -> list:
    splited_url = url.split("/")
    get_name = splited_url[3]
    return get_name

def get_name_lst (Url_links: list) -> list:
     for url in Url_links :
        result.append(get_n_f_s_l(url))
     return result 

print (get_name_lst(Url_links))

# def get_name_list  (Url_links: list, result: list ) -> list :
#     for url in Url_links :
    
#         splited_url = url.split("/")
#         get_name = splited_url[3 ]
#         result.append (get_name) 
#         print (result)
#         return result 
        
        
