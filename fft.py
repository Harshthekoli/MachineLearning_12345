import numpy as np
import matplotlib.pyplot as plt

# signal
t = np.linspace(0, 1, 500)
signal = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*20*t)

# FFT
fft_values = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=t[1]-t[0])

# only positive part
mask = frequencies > 0

plt.figure(figsize=(10, 5))
plt.plot(frequencies[mask], np.abs(fft_values[mask]))
plt.title("FFT - Frequency View of Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()