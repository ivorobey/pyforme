# mylist=[1,2,8,5,9]

# def targetnum(lst,target):
#     minn= min(lst, key=lambda x:abs(x-target))
#     maxx= max(lst, key=lambda x:abs(target+x))
#     return minn,maxx


# print(targetnum(mylist,4))
    
# print(abs(-2))

# def sum(x):return x+1
# lambda x:abs(x-target)
def lam(x,target):
    return abs(x-target)
    

print(lam(10,5))
