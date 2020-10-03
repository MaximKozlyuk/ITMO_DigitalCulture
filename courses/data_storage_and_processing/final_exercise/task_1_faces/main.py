# final exercise solution
import matplotlib.pyplot as plt

from courses.data_storage_and_processing.final_exercise.task_1_faces.CoordinatesDataFile import CoordinatesDataFile

# read all coordinates
data_file = CoordinatesDataFile(input("Enter path to file with coordinates:"))
xy, xz, xl, xr = data_file.read_coordinates()

plt.plot(xy[0], xy[1])
plt.plot(xz[0], xz[1])
plt.plot(xl[0], xl[1])
plt.plot(xr[0], xr[1])

plt.show()
