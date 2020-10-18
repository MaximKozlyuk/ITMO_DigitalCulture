# Агломеративная кластеризация   Опрос 4,5
from math import floor, ceil


class Object:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        super().__init__()

    def x(self) -> float:
        return self.__x

    def y(self) -> float:
        return self.__y

    def evklid_dist_to(self, point) -> float:
        return pow(
            pow(self.x() - point.x(), 2) + pow(self.y() - point.y(), 2), 1 / 2
        )

    def manheten_dist_to(self, point) -> float:
        return TaxiCabDist().dist((self.x(), self.y()), (point.x(), point.y()))

    def chebishev_dist_to(self, point) -> float:
        x = abs(point.x() - self.x())
        y = abs(point.y() - self.y())
        if x >= y:
            return x
        else:
            return y

    def __str__(self) -> str:
        return "[" + str(self.__x) + ", " + str(self.__y) + "]"


class Cluster:

    def __init__(self, objects) -> None:
        self.__objects = objects
        super().__init__()

    def objects(self) -> []:
        return list(self.__objects)

    def merge(self, objects):
        self.__objects.append(objects)

    def variation(self) -> float:
        raise Exception("not implemented")

    def full_connect_dist(self, cluster2) -> float:
        cluster2_objects = cluster2.objects()
        max_dist = 0.0
        for i in range(len(self.__objects)):
            for j in range(len(cluster2_objects)):
                current_dist = self.__objects[i].evklid_dist_to(cluster2_objects[j])
                if current_dist > max_dist:
                    max_dist = current_dist
        return max_dist

    def single_connect_dist(self, cluster2) -> float:
        cluster2_objects = cluster2.objects()
        min_dist = self.__objects[0].evklid_dist_to(cluster2_objects[0])
        for i in range(len(self.__objects)):
            for j in range(len(cluster2_objects)):
                current_dist = self.__objects[i].evklid_dist_to(cluster2_objects[j])
                if current_dist < min_dist:
                    min_dist = current_dist
        return min_dist

    def avg_connect_dist(self, cluster2) -> float:
        cluster2_objects = cluster2.objects()
        dist_sum = 0.0
        for i in range(len(self.__objects)):
            for j in range(len(cluster2_objects)):
                dist_sum += self.__objects[i].evklid_dist_to(cluster2_objects[j])
        return dist_sum / (len(self.__objects) * len(cluster2_objects))

    def centroid_dist(self, cluster2) -> float:
        return self.centroid().evklid_dist_to(cluster2.centroid())

    def centroid(self) -> Object:
        x_avg, y_avg = 0.0, 0.0
        for i in range(len(self.__objects)):
            x_avg += self.__objects[i].x()
            y_avg += self.__objects[i].y()
        x_avg /= len(self.__objects)
        y_avg /= len(self.__objects)
        return Object(x_avg, y_avg)

    # внутрикластерное расстояние
    def w(self) -> float:
        cluster_inner_dist = 0.0
        for i in range(len(self.__objects)):
            for j in range(len(self.__objects)):
                cluster_inner_dist += self.__objects[i].evklid_dist_to(self.__objects[j])
        return cluster_inner_dist

    # среднее внутрикластерное расстояние
    def avg_w(self) -> float:
        return self.w() / len(self.__objects)


# clustering from set of single object clusters
class HierarchicalCluster:

    # accepting [Object(1,2), Object(2,3) ...]
    def __init__(self, clusters) -> None:
        self.__clusters = clusters
        super().__init__()

    def do_clustering(self) -> None:
        return


class TaxiCabDist:

    def t(self, p, q) -> float:
        x, y = p
        z, w = q
        return abs(x - z) + abs(y - w)

    def corners(self, p) -> []:
        x, y = p
        if isinstance(x, float):
            return [(floor(x), y), (ceil(x), y)]
        else:
            return [(x, floor(y)), (x, ceil(y))]

    def dist(self, p, q) -> float:
        return min(self.t(p, c) + self.t(c, d) + self.t(d, q) for c in self.corners(p) for d in self.corners(q))


class LinealNorma:

    def __init__(self, arr) -> None:
        self.__arr = arr
        super().__init__()

    def normed_arr(self) -> []:
        norm = list(self.__arr)
        delta = max(self.__arr) - min(self.__arr)
        for i in range(len(norm)):
            norm[i] /= delta
        return norm
