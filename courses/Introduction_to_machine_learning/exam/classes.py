from courses.Introduction_to_machine_learning.classes import Object, Cluster

o1 = Object(1, 2)
o2 = Object(-2, 3)
o3 = Object(3, -1)

c1 = Cluster([o1])  # class 1
c2 = Cluster([o2, o3])  # class 0
center1 = c1.centroid()
center2 = c2.centroid()

test = Object(2, -3)

print(test.evklid_dist_to(center1))
print(test.evklid_dist_to(center2))

print()
print(test.evklid_dist_to(o1))
print(test.evklid_dist_to(o2))
print(test.evklid_dist_to(o3))