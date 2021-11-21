# def write():
#     a = [[1, 2, 3, 4], [2, 3, 4, 5, 6], "hjw"]
#     file_input = open("input.txt", 'w')
#     for b in a:
#         b_str = ""
#         if isinstance(b, list):
#             for c in b:
#                 b_str = b_str + str(c) + ','
#         else:
#             b_str = b
#         file_input.write(b_str + "\n")
#         print(b_str)
#     file_input.close()
#
#
# def read():
#     input_str_list = open("input.txt", 'r').readlines()
#     print(input_str_list)
#     input_list = list()
#     for input_str in input_str_list:
#
#         if input_str == 'hjw\n':
#             input_list.append('hjw')
#         else:
#
#             input_list.append(list(map(int, input_str.replace(',\n', '').split(","))))
#
#     print(input_list)

import json
import ast

a={}
b=[ast.Module, ast.Expr, ast.AST]
a['data']=b
a['author']='hjw'
print(a)

with open('input.json', 'w') as file:
    file.write(json.dumps(a))

# with open('input.json','r') as load_f:
#     load_dict = json.load(load_f)
#     print(load_dict)
#     for dict_ in load_dict:
#         print(dict_)
#         print(dict_['data'])
#         print(dict_['data'][0], dict_['data'][0][1])
