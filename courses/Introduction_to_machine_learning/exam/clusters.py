from courses.Introduction_to_machine_learning.classes import Object

c1 = Object(1, 2)
c2 = Object(-2, 3)
c3 = Object(3, -1)

test = Object(2, -3)

print(pow(test.evklid_dist_to(c1), 2))
print(pow(test.evklid_dist_to(c2), 2))
print(pow(test.evklid_dist_to(c3), 2))
