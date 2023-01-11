import matplotlib.pylab as plt
import pandas as pd
import numpy as np

data  = pd.read_csv("Book1.csv")
print(data.head(12))

sample = data[0:40]
plt.plot(sample['Year Built'],sample['Site EUI (kBtu/ft)'])
plt.xticks(rotation=45)

plt.xlabel('year')
plt.ylabel('EUI')
plt.title("change1da")

plt.show()


fig = plt.figure(figsize =(6,9))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,4)

ax1.plot(np.random.randint(1,5,5),np.arange(5))
ax2.plot(np.arange(10)*3,np.arange(10))
plt.show()


fig = plt.figure(figsize =(9,9) )
for i in range(2):
    label1 = str(2021+i)
    plt.plot(sample[0:6]['Year Built'],sample[0:6]['Site EUI (kBtu/ft)'],c='red',label = label1)
    plt.plot(sample[6:12]['Year Built'],sample[6:12]['Site EUI (kBtu/ft)'],c='blue',label = label1)
plt.legend(loc='best')
plt.show()


col =['','','','','']
data1 = data[col]
height = data1.ix[0,col].value
position = range(5)+0.75

fig, ax = plt.subplots()
ax.bar(position,height,0.3)
# ax.barh(position,height,0.3)
# ax.scatter(position,height)
# ax.hist(data[""],range=(4,5),bin=30)
# ax.set_ylim(0,50)
# ax.boxplot(data[""],)
plt.show()