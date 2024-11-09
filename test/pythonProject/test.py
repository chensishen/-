import matplotlib.pyplot as plt
import random
x = range(60)
y = [random.uniform(15,18) for i in x]
plt.figure(figsize=(20,8),dpi=100)
plt.plot(x,y)

x_ticks_label = ["11点{}分".format(i) for i in x]
y_ticks = range(40)

# plt.xticks(x_ticks_label[::5])
plt.xticks(x[::5],x_ticks_label[::5])
plt.yticks(y_ticks[::5])

plt.show()