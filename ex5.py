import numpy as np
import matplotlib.pyplot as plt

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Compute the FFT of the signal
fft_result = np.fft.fft(signal)

# Compute the magnitude and phase spectrum of the FFT result
magnitude_spectrum = np.abs(fft_result)

phase_spectrum = np.angle(fft_result)

# Compute the IFFT of the FFT result
reconstructed_signal = np.fft.ifft(fft_result)

# Display results
print("Original Signal:")
print(signal)

print("\nFFT Result:")
print(fft_result)

print("\nMagnitude Spectrum:")
print(magnitude_spectrum)

print("\nPhase Spectrum:")
print(phase_spectrum)

print("\nReconstructed Signal:")
print(reconstructed_signal)

# Plot the results
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(signal)
plt.title("Original Signal")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.stem(magnitude_spectrum)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.subplot(3, 1, 3)
plt.stem(np.real(reconstructed_signal))
plt.title("Reconstructed Signal using IFFT")
plt.xlabel("Sample")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()