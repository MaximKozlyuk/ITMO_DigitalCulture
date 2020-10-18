# ans try:
# 1) 193, 70.105, 1.262, 1, None, None (все неверно)
# 2)

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from courses.Introduction_to_machine_learning.classes import LinealNorma

column_names = ["MIP", "STDIP", "EKIP", "SIP", "MC", "STDC", "EKC", "SC", "TARGET"]
data = pd.read_csv('./selection.csv', delimiter=',', names=column_names)
mip_str = data.MIP.to_list()[1:]
mip = []
for i in range(len(mip_str)):
    mip.append(float(mip_str[i]))


def str_arr_to_float(arr) -> []:
    for arr_i in range(len(arr)):
        arr[arr_i] = float(arr[arr_i])
    return arr


# нормировка всех столбцов
normed_data_not_transposed = [
    str_arr_to_float(data.MIP.to_list()[1:]),
    str_arr_to_float(data.STDIP.to_list()[1:]),
    str_arr_to_float(data.EKIP.to_list()[1:]),
    str_arr_to_float(data.SIP.to_list()[1:]),
    str_arr_to_float(data.MC.to_list()[1:]),
    str_arr_to_float(data.STDC.to_list()[1:]),
    str_arr_to_float(data.EKC.to_list()[1:]),
    str_arr_to_float(data.SC.to_list()[1:]),
]
for i in range(len(normed_data_not_transposed)):
    normed_data_not_transposed[i] = LinealNorma(normed_data_not_transposed[i]).normed_arr()
normed_data = np.transpose(normed_data_not_transposed).tolist()

print("Выборочное среднее MIP после нормировки:",
      sum(normed_data_not_transposed[0]) / len(normed_data_not_transposed[0]))

y = str_arr_to_float(data.TARGET.to_list()[1:])
reg = LogisticRegression(random_state=2019, solver='lbfgs').fit(normed_data, y)

new_star = [[0.539, 0.162, 0.188, 0.653, 0.796, 0.233, 0.397, 0.065]]
print("New star prediction: ", reg.predict(new_star))

# Введите расстояние от новой звезды до ближайшего соседа, используя евклидову метрику.
