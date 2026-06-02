import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Generate signal
t = np.linspace(0, 1, 500, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t)+ 0.5 * np.random.normal(size=t.shape) 

# Butterworth low-pass filter
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    return lfilter(b, a, data)

# Apply filter
cutoff_frequency = 10
sampling_rate = 500
filtered_signal = lowpass_filter(signal, cutoff_frequency, sampling_rate)

# 📊 PLOTTING
plt.figure(figsize=(10, 6))

plt.plot(t, signal, label="Noisy Signal", alpha=0.5)
plt.plot(t, filtered_signal, label="Filtered Signal", linewidth=2)

plt.title("Signal Filtering (Low-Pass Butterworth Filter)")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.show()