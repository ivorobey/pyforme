

# with open('names.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

import csv
import string
import random



def generator(size=1024,chars=string.ascii_lowercase+string.digits):
    return ["".join(random.choice(chars)for _ in range(size))]
    

mylist=generator()

print(mylist)


lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
for el in mylist:
    a=lol(el,8)

print(a)





# with open('list_to_csv.csv','w') as csvfile:
#     csvwriter=csv.writer(csvfile)
#     for item in a:
#         csvwriter.writerow([item])









