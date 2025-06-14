# import time

# start = time.time()

# for i in range(1,101):
#     print(i)

# print(time.time()- start)

# 1 but this is not used in industry for measuring time  . so we have to avoid it.

# import time

# start = time.time()
# i = 1
# while i < 101:
#     print(i)
#     i +=1

# print(time.time()-start)

# # 2 this is also not the exict way to measure the time so avoid it

# note = """""1Biscally there are three way of measuring time of a code the first one that we learned is above 
# but we should not used this method becuase it change in different situtation so avoid it
# 2 counting the operation  involved 
# 3 abstract notion of order of growth"""

# def binary_search(arr, target):
#     left , right = 0 , len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1
#     return -1

# arr = [1,2,3,4,5,6,7,8,9]
# target= 4

# result = binary_search(arr,target)
# print(result)

def sum_digits(num):

    sum = 0
    while (num > 0):
        sum += num%10
        num/=10
    return sum
print(sum_digits(123))

