import matplotlib.pyplot as plt

labels = 'frogs', 'hogs', 'dogs', 'logs'

data =[15, 30, 45, 10] # 100%

figl, axl=plt.subplots() #grafik
axl.pie(data, labels=labels, shadow=True)
plt.show()