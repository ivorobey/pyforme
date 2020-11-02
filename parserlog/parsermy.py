
api_list=list()
api_name_time=list()
string="<[s] API exit> END"

def parser(filename):

    #парсим файл и добавляем в масив api_list
    with open(filename) as f:
        for line in f:
            if(line.find(string)>0):
                api_list.append(line)
    
    #записываем масив в новый файл
    with open('parse_console.log','a') as f:
        for line in api_list:
            f.write(line)



def name_time_parser(filename):
    #парсим файл, находим имя и время и добавляем в масив api_name_time
    with open(filename) as f:
        for line in f:
            a, nameapi, c = line.split('"')
            if ')' in c:
                trash, timeanswer = c.split(')')
                timeanswer = timeanswer.replace(' ms', '').replace(' ', '')
            else:
                timeanswer = c.replace(' ms', '').replace(' ', '')
            api_name_time.append('Name API: '+ nameapi)
            api_name_time.append('Time: '+timeanswer)
            
    
    #записываем масив в новый файл   
    with open('api_name_time.log','a') as f:
       for line in api_name_time:
           f.write(line+"\n")


            
       


if __name__=='__main__':
    #parser('console.log')
    name_time_parser('parse_console.log')



