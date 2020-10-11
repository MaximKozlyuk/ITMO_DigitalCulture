# расчеты: простейшая линейная регрессия

x_arr = [13.0, 4.0, 11.0, 20.0]
y_arr = [8.0, 5.0, 6.0, 15.0]
n = 4.0

x_1 = 12.0
y = 8.5

top, bot = 0.0, 0.0
for i in range(len(x_arr)):
    top += (x_arr[i] - x_1) * (y_arr[i] - y)
    bot += pow(x_arr[i] - x_1, 2)
tetta_1 = top / bot

# 1.28125
# -6.875
print(tetta_1)
tetta_0 = y - tetta_1 * x_1
print(tetta_0)

eps = 0.05

print("1 - eps/2 = ", 1 - eps / 2)

top1, bot2 = 0.0, 0.0
for i in range(len(y_arr)):  # calculate SE(o0)
    top1 += pow(y_arr[i] - tetta_0 - tetta_1 * x_arr[i], 2)
    bot2 += pow(x_arr[i] - x_1, 2)

se_tetta_0 = pow(top1 / (n - 2), 1 / 2) * pow(1 / n + pow(x_1, 2) / bot2, 1 / 2)
print(se_tetta_0)

se_tetta_1 = pow(top1 / (n - 2), 1 / 2) * pow(1 / bot2, 1 / 2)
print(se_tetta_1)

t_eps = 4.303

di_tetta0_bot = tetta_0 - t_eps * se_tetta_0
di_tetta0_top = tetta_0 + t_eps * se_tetta_0

di_tetta1_bot = tetta_1 - t_eps * se_tetta_1
di_tetta1_top = tetta_1 + t_eps * se_tetta_1

print(di_tetta0_bot, " ", di_tetta0_top)
print(di_tetta1_bot, " ", di_tetta1_top)

t = abs(tetta_1) / se_tetta_1
print("t =", t)

rse_sum = 0.0
r_square_y_sum = 0.0
for i in range(len(x_arr)):
    rse_sum += pow(y_arr[i] - tetta_0 - tetta_1 * x_arr[i], 2)
    r_square_y_sum += pow(y_arr[i] - y, 2)
RSE = pow((1 / (n - 2)) * rse_sum, 1 / 2)
print("RSE = ", RSE)

r_square = 1 - (rse_sum / r_square_y_sum)
print("R^2 = ", r_square)
