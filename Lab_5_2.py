num_lst0 = [i for i in range(10)]
num_lst1 = [i for i in range(0, 10, 2)]
num_lst2 = []

def intersection(arg1, arg2):
    res = []
    for l in arg1:
        if l in arg2:
            res.append(l)
    return res

def intersection_lst(lst0, lst1):
    return(list(set(lst0) & set(lst1)))

print(num_lst0, num_lst1, num_lst2)
print(intersection_lst(num_lst1, num_lst0))
print(intersection(num_lst1, num_lst0))