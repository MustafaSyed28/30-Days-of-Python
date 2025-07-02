def reverse_R(arr, index=None):
    if index is None:
        index = len(arr) - 1
    if index < 0:
        return
    print(arr[index])
    reverse_R(arr, index - 1)

print("Recursive Reverse Print:")
reverse_R([10, "mustafa", 30, "apple"])



def reverse_I(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])

print("Iterative Reverse Print:")
reverse_I([10, 20, 30])

