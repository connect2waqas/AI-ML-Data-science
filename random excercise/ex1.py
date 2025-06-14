arr = [10, 20, 30, 40, 50]
left, right = 0, len(arr) - 1

while left <= right:
    print("left:",arr[left],"Right:",arr[right])
    left +=1
    right -=1
