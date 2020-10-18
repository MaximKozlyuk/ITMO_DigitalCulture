# k-NN method
from courses.Introduction_to_machine_learning.classes import Object

objects = [Object(28, 10),
           Object(49, 49),
           Object(48, 35),
           Object(36, 33),
           Object(45, 54)]

o = Object(33, 47)

min_evklid_dist = [o.evklid_dist_to(objects[0]), 0]
min_manheten_dist = [o.manheten_dist_to(objects[0]), 0]
min_chebishev_dist = [o.chebishev_dist_to(objects[0]), 0]
for i in range(len(objects)):
    if min_evklid_dist[0] < o.evklid_dist_to(objects[i]):
        min_evklid_dist[0] = o.evklid_dist_to(objects[i])
        min_evklid_dist[1] = i
    if min_manheten_dist[0] < o.manheten_dist_to(objects[i]):
        min_manheten_dist[0] = o.manheten_dist_to(objects[i])
        min_manheten_dist[1] = i
    if min_chebishev_dist[0] < o.chebishev_dist_to(objects[i]):
        min_chebishev_dist[0] = o.chebishev_dist_to(objects[i])
        min_chebishev_dist[1] = i

print(min_evklid_dist)
print(min_manheten_dist)
print(min_chebishev_dist)

# weight calculation wi = 1 / (evk_dist i)^2
sum_weight_0_class, sum_weight_1_class = 0.0, 0.0
for i in range(len(objects)):
    if i == 2 or i == 4:
        sum_weight_0_class += 1 / pow(o.evklid_dist_to(objects[i]), 2)
    else:
        sum_weight_1_class += 1 / pow(o.evklid_dist_to(objects[i]), 2)

print(sum_weight_0_class)
print(sum_weight_1_class)
