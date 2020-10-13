import matplotlib.pyplot as plt
import pandas as pd

from courses.Introduction_to_machine_learning.k_neighbours.classes import Dot

data = pd.read_csv('./example_data.csv', delim_whitespace=True, index_col='id')

x = data['X'].tolist()
y = data['Y'].tolist()
classes = data[data.columns[2]].tolist()

obj = Dot(33.0, 47.0)
dots = []
for i in range(len(x)):
    dots.append(Dot(x[i], y[i]))

evklid_min_dist = []
manhetn_min_dist = []
chebisheva_min_dist = []
for i in range(len(dots)):
    evklid_min_dist.append(obj.evklid_dist_to(dots[0]))
    manhetn_min_dist.append(obj.manheten_dist_to(dots[0]))
    chebisheva_min_dist.append(obj.chebisheva_dist_to(dots[0]))
evklid_min_dist = min(evklid_min_dist)
manhetn_min_dist = min(manhetn_min_dist)
chebisheva_min_dist = min(chebisheva_min_dist)

print("Min distances:")
print(evklid_min_dist)
print(manhetn_min_dist)
print(chebisheva_min_dist)

plt.plot(x, y, 'ro')
plt.plot([33], [47], 'bo')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
