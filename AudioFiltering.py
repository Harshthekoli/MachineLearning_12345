from scipy.io import wavfile
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# load audio
fs, data = wavfile.read("complex_audio.wav")

# normalize if stereo
if len(data.shape) > 1:
    data = data[:, 0]

# filter
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    norm = cutoff / nyq
    b, a = butter(order, norm, btype='low')
    return b, a

def filter_audio(data, cutoff, fs):
    b, a = butter_lowpass(cutoff, fs)
    return lfilter(b, a, data)

filtered = filter_audio(data, 1000, fs)

# plot
plt.plot(data[:1000], label="Original")
plt.plot(filtered[:1000], label="Filtered")
plt.legend()
plt.title("Audio Filtering")
plt.show()