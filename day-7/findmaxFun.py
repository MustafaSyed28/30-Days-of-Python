def find_max_iterative(lst):
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

b= find_max_iterative([2,3,4,5,6])
print(b)


def find_max_recursive(lst):
    if len(lst) == 1:
        return lst[0]

    max_res = find_max_recursive(lst[1:])
    return lst[0] if lst[0] > max_res else max_res

print(find_max_recursive([2,3,4,5,6]))