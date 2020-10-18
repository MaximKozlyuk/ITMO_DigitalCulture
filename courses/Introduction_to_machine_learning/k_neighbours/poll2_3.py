from courses.Introduction_to_machine_learning.classes import Object, Cluster

objects = [Object(1, 2), Object(0, 3), Object(-1, 1)]
c1 = Cluster(objects)
c1_centroid = c1.centroid()
c2_centroid = Object(2, -3)
x = Object(4, 0)
x_cluster_num = (2, 1)[x.evklid_dist_to(c1_centroid) < x.evklid_dist_to(c2_centroid)]

print("W =", c1.w())
print("avg W =", c1.avg_w())
print("C1 centroid =", c1_centroid)
print(x_cluster_num)

# посдтавить нужный кластер
print(pow(x.evklid_dist_to(c2_centroid), 2))
