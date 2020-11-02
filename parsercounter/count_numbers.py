import re

#USE for numbers1.txt
def parser(filename):
    numbers_list=list()
    #парсим файл и добавляем элементы в масив numbers_list
    with open(filename) as f:
        for line in f:
            numbers_list.append(line)

    #преобразовываем в масив интов
    for i,elem in enumerate(numbers_list):
        numbers_list[i]=int(elem)


    #выводим сумму всех элементов
    print(sum(numbers_list))


#Use for numbers2.txt
def parser2(filename):
    #регуляркой отсекаем все лишнее (pythex.org использовал)
    data=open(filename).read()
    reg=r'[0-9]+[.]+[0-9]+[0-9]'
    nums=re.findall(reg,data)
    #переводим в масив поплавок
    float_nums=[float(x)for x in nums]
    

    print(sum(float_nums))
   


if __name__=='__main__':
    parser('numbers1.txt')
    parser2('numbers2.txt')
    
