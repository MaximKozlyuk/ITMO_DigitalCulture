# Агломеративная кластеризация   Опрос 4
class Object:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y
        super().__init__()

    def x(self) -> float:
        return self.__x

    def y(self) -> float:
        return self.__y

    def evklid_dist_to(self, dot) -> float:
        return pow(
            pow(self.x() - dot.x(), 2) + pow(self.y() - dot.y(), 2), 1 / 2
        )


class Cluster:

    def __init__(self, objects) -> None:
        self.__objects = objects
        super().__init__()

    def objects(self) -> []:
        return list(self.__objects)

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
