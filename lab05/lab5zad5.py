import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import buttord, butter, freqresp

def filtr(f_pass, f_stop, f_center, title):
    wp = [(f_center - f_pass) * 2 * np.pi, (f_center + f_pass) * 2 * np.pi]
    ws = [(f_center - f_stop) * 2 * np.pi, (f_center + f_stop) * 2 * np.pi]
    gpass = 3; gstop = 40
    n, wn = buttord(wp, ws, gpass, gstop, analog=True) # najmniejszt rzad filru Butterwortha
    print(f"{title}: Rząd filtru: {n}")

    # projektowanie
    b, a = butter(n, wn, btype='band', analog=True)

    f = np.linspace(f_center - 2e6, f_center + 2e6, 10000)
    w = 2 * np.pi * f
    w, h = freqresp((b, a), w)


    plt.plot(f, 20 * np.log10(np.abs(h)), label='|H(f)| [dB]')
    plt.axvline(f_center - f_pass, color='green', linestyle='--', label='Pasmo przepustowe')
    plt.axvline(f_center + f_pass, color='green', linestyle='--')
    plt.axvline(f_center - f_stop, color='orange', linestyle='--', label='Pasmo zaporowe')
    plt.axvline(f_center + f_stop, color='orange', linestyle='--')
    plt.axhline(-3, color='red', linestyle='--', label='-3 dB')
    plt.axhline(-40, color='purple', linestyle='--', label='-40 dB')
    plt.title(f'{title}')
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Wzmocnienie [dB]')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

f_center = 96e6

#testowy
filtr(f_pass=1e6, f_stop=2e6, f_center=f_center, title='Testowy filtr: 96 MHz ±1 MHz')

# docelowy
filtr(f_pass=1e5, f_stop=3e5, f_center=f_center, title='Docelowy filtr: 96 MHz ±100 kHz')
