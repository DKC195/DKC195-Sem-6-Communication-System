import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

def plot_sine_wave(frequency):
    # Define the range for x values
    x_values = np.linspace(0, 2*np.pi, 100)
    
    # Calculate y values for the sine wave
    y_values = np.sin(frequency * x_values)
    
    # Plot the sine wave using stem plot
    ax.clear()
    ax.stem(x_values, y_values, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.set_title(f'Sine Wave with Frequency {frequency} Hz')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    plt.draw()

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Create text box widget for frequency input
ax_frequency = plt.axes([0.1, 0.01, 0.8, 0.05])
text_box_frequency = TextBox(ax=ax_frequency, label='Frequency (Hz)', initial='1')

# Define function to update plot when text box value changes
def update_frequency(text):
    frequency = float(text)
    plot_sine_wave(frequency)

# Register the callback function with the text box widget
text_box_frequency.on_submit(update_frequency)

plt.show()
