# # 1
# def summa(x, y):
#     num = 0
#     for i in range(x+1, y):
#         num += i
#     return num
#
# print(summa(2, 5))

# # 2
# def summa():
#     num = 0
#     for i in range(1, 100):
#         if i % 2 == 0:
#             num += i
#     return num
#
# print(summa())


# # 3
# def string(string):
#     res = ""
#     for i in string:
#         res += (f"{i} \n")
#     return res
# print(string("Hello"))


# # 4
# def even_list(lst):
#     new_lst = []
#     for i in lst:
#         if i % 2 == 0:
#             new_lst.append(i)
#     return new_lst
#
# print(even_list([2, 3, 4, 5, 6, 7]))


# # 5
# def upper_strings(lst):
#     new_lst = []
#     for i in lst:
#         if i[0] != i[0].lower():
#             new_lst.append(i)
#     return new_lst
#
# print(upper_strings(["Hello", "world", "Hi"]))


# # 6
# def python_strings(lst):
#     new_lst = []
#     for i in lst:
#         if "Python" in i:
#             new_lst.append(i)
#     return new_lst
#
# print(python_strings(["Hello", "world", "Hi, Python", "python"]))

# # 7
# dictionary = {}
#
# def add_word(word, definition):
#     dictionary[word] = definition
#     print(f"{word}: {dictionary[word]} was added to the list")
#
# def del_word(word):
#     if word in dictionary:
#         del dictionary[word]
#         print(f"{word} was deleted from the dictionary")
#     else:
#         print(f"{word} is not in the dictionary")
#
# def search(word):
#     if word in dictionary:
#         print(dictionary[word])
#     else:
#         print(f"{word} is not in the dictionary")
#
# add_word("Python", "Programming language")
# del_word("Python-2")
# search("Python")

# # 8
# lst = [(2, 1), (3, 8), (2, 2), (2, 4)]
# sorted_lst = sorted(lst, key=lambda x: x[1])
# print(sorted_lst)




