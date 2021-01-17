readed = open('data.txt', 'r')
data =[]
temp=[]
date=[]
for i in readed:
    #data.append(i[:-5])
    #temp.append(i[:-5])
    data.append(i[0:3])
    date.append(i[2:-5])

#print(temp)
print(data)
print(date)

readed.close()