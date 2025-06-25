def sorted_R(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return sorted_R(arr, index + 1)

print("Recursive Sorted Check:", sorted_R([1, 2, 3, 4]))



def sorted_I(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

print("Iterative Sorted Check:", sorted_I([1, 2, 0, 4]))
