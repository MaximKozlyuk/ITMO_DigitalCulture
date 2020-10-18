import matplotlib.pyplot as plt

from courses.Introduction_to_machine_learning.classes import Cluster, Object

cluster1 = Cluster([
    Object(1, 2), Object(0, 3), Object(-1, 1)
])
cluster2 = Cluster([
    Object(0, -4), Object(4, -2)
])

print(cluster1.full_connect_dist(cluster2))
print(cluster1.single_connect_dist(cluster2))
print(cluster1.avg_connect_dist(cluster2))
print(cluster1.centroid_dist(cluster2))

print("Опрос 5.")
o1 = Object(-1, 1)
o2 = Object(0, -4)
o3 = Object(4, -2)
print(o1.evklid_dist_to(o2))
print(o1.evklid_dist_to(o3))
print(o2.evklid_dist_to(o3))

x = [1, 0, -1, 0, 4]
y = [2, 3, 1, -4, -2]
plt.plot(x, y, 'ro')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

# x_2;x_1
# x_2,x_1;x_3
# x_4;x_5
# x_2,x_1,x_3;x_4,x_5
