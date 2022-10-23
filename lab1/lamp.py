import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def main():
    df = pd.read_csv('lamp_data.csv', dtype=float, header=0)
    V = np.asarray(df.get('V'))
    I = np.asarray(df.get('I'))
    Vs = np.asarray(df.get('Rad'))

    R_0 = 0.278  # [Ohm]
    R = V / I

    delta_V = 0.01
    delta_I = 0.001
    delta_R = np.sqrt((delta_V / I)**2 + (delta_I * V / I ** 2)**2)
    avg_delta_R_R = np.average(delta_R / R)

    print(f'{avg_delta_R_R:.2%}')

    print(R/R_0)

    # From table in Kelvin:
    delta_T = 50.
    T = np.asarray(
        [900, 1400, 1600, 1700, 1900, 2100,
        2300, 2400, 2500, 2600, 2700, 2800],
        dtype=float
    )
    delta_T_4 = np.sqrt((4 * T ** 3 * delta_T)**2)
    print(f'{delta_T_4[0]:.2e}\n{(T[0])**4:.2e}')
    # exit()

    line = linregress(x=T**4, y=Vs)
    a = line.slope
    b = line.intercept

    plt.errorbar(x=T**4, xerr=delta_T_4, y=Vs, yerr=0.1, label='$V_s(T^4)$', color='k')
    plt.plot(T**4, a*T**4 + b, color='k', ls='--', label=f'{a:.2e} T$^4$ + {b:.2f}')
    plt.xlabel('$T^4$ [K$^4$]', fontsize=14)
    plt.ylabel('Radiation intensity $V_s$ [mV]', fontsize=14)
    plt.title('Radiation from Tungsten lamp', fontsize=18)
    plt.text(0, 26, f'R-value: {line.rvalue:.2e}')
    plt.legend(loc='lower right')
    plt.grid()
    plt.savefig('lamp.pdf')
    plt.show()

if __name__ == '__main__':
    main()
