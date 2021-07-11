import math

from courses.Introduction_to_machine_learning.classes import Object

c1 = Object(1, -1)
c2 = Object(2, -6)
c3 = Object(7, 7)

test = Object(3, -7)

print(pow(test.evklid_dist_to(c1), 2))
print(pow(test.evklid_dist_to(c2), 2))
print(pow(test.evklid_dist_to(c3), 2))

print(0.095 - 0.424 * 4 + 0.956 * 3)
print(1 / (1 + pow(math.e, -1.267)))

arr = [9, 1, 1, 8, 7, 7, 3, 6, 6]
print(sum(arr) / len(arr))
