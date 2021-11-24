
l = [1, 4, 8, 3, 10, 5, 11,999]

# lambda - это анонимная функция которая часто используется в таких функциях, как sorted()\ min
# которые принимают вызываемый объект в качестве параметра (часто параметр ключевого слова key )


def search_min_max(lst, target):
    try:
        if target == max(lst):
            lower = min([i for i in lst if i < target ], key=lambda x: abs(x-target))
            return lower,target
        elif target == min(lst):
            upper = min([i for i in lst if i > target ], key=lambda x: abs(x-target))
            return upper,target
        else:
            lower = min([i for i in lst if i < target ], key=lambda x: abs(x-target))
            upper = min([i for i in lst if i > target ], key=lambda x: abs(x-target))
        return lower ,upper 
    except ValueError: # if target > max(lst) or target < min(lst)
        return None
 


print(search_min_max(l, 9))
