import scipy.special as sc
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

# замены для удобства
pi = math.pi
sqrt = math.sqrt
atan = math.atan
ln =  cmath.log
atan = cmath.atan
exp = cmath.exp
cos = math.cos
sin = math.sin

def generate_circl(R, N):
    dphi_grad = 360 / N  # угловой шаг на круга [град]
    dphi_rad = math.radians(dphi_grad)  # угловой шаг на круга [рад]
    dx = 2 * a * math.sin(dphi_rad / 2)


    # создадим пустые массивы
    dx_mass = [];
    phi_grad_circl = [];
    x_midle, z_midle = [];
    tx, tz = [];
    nx, nz = [];

    for i in range(N):
        # текущий угол для круга
        cur_phi_grad = i * dphi_grad
        cur_phi_rad = i * dphi_rad

        # cохраним угол в градусах в массив (для графика)
        phi_grad_circl.append(cur_phi_grad)

        # посчитаем координаты через угол в радианах
        zi = R * sin(cur_phi_rad)
        xi = R * cos(cur_phi_rad)

        # упакуем их в массив
        x_midle.append(xi)
        z_midle.append(zi)

    coord = [x_midle, z_midle];
    tau = 0;
    norm = 0;
    phi_grad_circl = 0;
    dx_mass = 0;
    return [coord, tau, norm, phi_grad_circl, dx_mass]

