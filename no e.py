import numpy as np
import matplotlib.pyplot as plt

# Define the signal parameters
f1 = 50  # Frequency of the first sine wave (Hz)
f2 = 120  # Frequency of the second sine wave (Hz)
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector from 0 to 1 second with a step of 1/fs

# Generate the signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute the FFT
S = np.fft.fft(s)
N = len(S)
frequencies = np.fft.fftfreq(N, 1/fs)

# Plot the signal
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Time-Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot the frequency spectrum
plt.subplot(2, 1, 2)
plt.stem(frequencies[:N//2], np.abs(S)[:N//2] * 2 / N, use_line_collection=True)
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
