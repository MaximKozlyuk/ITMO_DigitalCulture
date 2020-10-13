from courses.Introduction_to_machine_learning.agglomerative_clustering.classes import Cluster, Object

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
