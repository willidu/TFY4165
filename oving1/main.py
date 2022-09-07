"""
Solution to task (e) in Øving 1.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def T(z, const_temp):
    temp = 234.  # K
    if not const_temp:
        temp += 14. * np.exp(-2.*z) - 2.25 * z
    return temp

def H(z, const_temp):
    return 8.314 * T(z, const_temp) / (43.34 * 3.71)

def p(z, p0, const_temp=False):
    return p0 * np.exp(-1. * quad(lambda z, const_temp: 1. / H(z, const_temp), 0, z, args=(const_temp))[0])

def main():
    p0 = 600.  # [Pa]
    N = 1000
    z_arr = np.linspace(0, 16, N)
    p_arr = np.zeros_like(z_arr)
    p_arr_const_temp = np.zeros_like(z_arr)

    for i, z in enumerate(z_arr):
        p_arr[i] = p(z, p0)
        p_arr_const_temp[i] = p(z, p0, const_temp=True)

    plt.plot(z_arr, p_arr, label='Varying T')
    plt.plot(z_arr, p_arr_const_temp, label='Constant T = 234')
    plt.title('Atmospheric pressure on Mars')
    plt.xlabel('Elevation [km]')
    plt.ylabel('Pressure [Pa]')
    plt.legend()
    plt.grid()

if __name__ == '__main__':
    main()
    plt.show()
