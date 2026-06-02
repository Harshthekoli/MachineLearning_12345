import numpy as np
import matplotlib.pyplot as plt

# 1. Create time axis
t = np.linspace(0, 1, 500)

# 2. Clean signal (sine wave)
clean_signal = np.sin(2 * np.pi * 5 * t)

# 3. Noise
noise = np.random.randn(500) * 0.5

# 4. Noisy signal
noisy_signal = clean_signal + noise

# 5. Mean and std
mean_val = np.mean(noisy_signal)
std_val = np.std(noisy_signal)

# 6. Plot
plt.figure(figsize=(10, 5))

plt.plot(t, clean_signal, label="Clean Signal", linewidth=2)
plt.plot(t, noisy_signal, label="Noisy Signal", alpha=0.6)

# mean line
plt.axhline(mean_val, color='red', linestyle='--', label=f"Mean = {mean_val:.2f}")

# std lines (±1 std range)
plt.axhline(mean_val + std_val, color='green', linestyle='--', label="+1 Std")
plt.axhline(mean_val - std_val, color='green', linestyle='--', label="-1 Std")

plt.title("Clean vs Noisy Signal + Mean & Std")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()