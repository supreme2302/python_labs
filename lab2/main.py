from first import Friends
from second import GetId
import datetime
import matplotlib.pyplot as plt

name=input()
today = datetime.datetime.today()
id=GetId().response_handler(name)
age=Friends().response_handler(id)
a=[]
for i in age:
    if ('bdate' not in i):
        continue
    if (len(i['bdate']) > 5):
        # print(i)
        d = datetime.datetime.strptime(i['bdate'], "%d.%m.%Y")
        # t=datetime.timedelta(d.day)
        y = int((str((today - d) / 365)[0:2]))

        a.append(y)
#print(a)



plt.hist(
    a, # в зависимости от количества 1,2,3 строится гистограмма
    40 # а это как бы длина оси х
    )
plt.show()