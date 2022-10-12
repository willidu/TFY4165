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

    print(R/R_0)

    # From table in Kelvin:
    T = np.asarray(
        [900, 1400, 1600, 1700, 1900, 2100,
        2300, 2400, 2500, 2600, 2700, 2800],
        dtype=float
    )

    line = linregress(x=T**4, y=Vs)
    a = line.slope
    b = line.intercept

    plt.plot(T**4, Vs, color='k', ls='-', label='$V_s(T^4)$')
    plt.plot(T**4, a*T**4 + b, color='k', ls='--', label=f'{a:.2e} T$^4$ + {b:.2f}')
    plt.xlabel('$T^4$ [K]', fontsize=14)
    plt.ylabel('Radiation intensity $V_s$ [mV]', fontsize=14)
    plt.title('Radiation from Wolfram lamp', fontsize=18)
    plt.text(0, 26, f'R-value: {line.rvalue:.2e}')
    plt.legend(loc='lower right')
    plt.grid()
    plt.savefig('lamp.pdf')
    plt.show()

if __name__ == '__main__':
    main()
