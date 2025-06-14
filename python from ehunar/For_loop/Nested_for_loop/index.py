# list1= [1,2,3]

# list2 =["a","b","c"]

# for x in list1:
#     for y in list2:
#         print(x,y)



# # Multiplication table using nested for loops

# # Outer loop for rows
# for i in range(1, 6):
#     # Inner loop for columns
#     for j in range(1, 6):
#         print(f'{i * j:2}', end=' ')
#     print()


# practice question No 1

# Multiplication table for the number 2 using nested for loops

# for i in range(1, 11):
    
#     for j in range(2, 3):  
#         print(f'{j} x {i} = {j * i}')\\

# table for 10

# for n in range(1,11):
#     for m in range(10,11):
#         print(f"{n} x {m}={n*m}")

# table for 20

# for i in range(1,21):
#     for j in range(20,21):
#         print(f"{i}x{j}={i*j}")


# genrate through another method

# num1 =[2]

# num2 =[1,2,3,4,5,6,7,8,9,10]

# for n in num1:
#     for m in num2:
#         print(f"{ n } x {m}={n * m}")
for n in range(1,101):
    for m in range(1,101):
        print(f"{n}x{m}={n*m}")