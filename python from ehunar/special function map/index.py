# # Special function Map
# li = [1,2,3]

# def adder_map(para_li):
#     return para_li+1

# print(list(map(adder_map,li)))


# # li =[1,2,3]
# new_li= []
# def my_list(para_li):
#     for i in para_li:
#         new_li.append(i+1)
#     return new_li
# print(my_list(li))

    
    
def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(add, numbers1, numbers2)

print(list(result))  # Output: [5, 7, 9]
