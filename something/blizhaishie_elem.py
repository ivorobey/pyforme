
l = [1, 4, 8, 3, 10, 5, 11]

# lambda - это анонимная функция которая часто используется в таких функциях, как sorted()\ min
#       которые принимают вызываемый объект в качестве параметра (часто параметр ключевого слова key )


def search_min_max(lst, target):
    lower = min([i for i in lst if i < target], key=lambda x: abs(x-target))
    upper = min([i for i in lst if i >= target], key=lambda x: abs(x-target))
    return lower, upper


print(search_min_max(l, 9))
