def findsmall(arr):
    smallest=arr[0] #храним наименьш знач
    smallest_index=0 #храним индекс наименш знач
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index


def slectionSort(arr): #сортирруем масив
    newArr=[]
    for i in range(len(arr)):
        smallest=findsmall(arr) #находим наименьш элемент и добавляем в новый масив
        newArr.append(arr.pop(smallest))
    return newArr

print(slectionSort([5,3,6,2,10]))