import time
import numpy as np
import sounddevice as sd
import os
import subprocess
from screeninfo import get_monitors
import pyautogui

def beep(frequency, duration, volume=1.0, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

def get_monitor_info():
    monitors = get_monitors()
    for i, monitor in enumerate(monitors):
        print(f"Monitor {i}: {monitor}")
    return monitors

def open_safari_with_url(url):
    subprocess.run(["open", "-a", "Safari", url])

def click_at_position(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    print(f"Clicked at position ({x}, {y})")

# Get monitor information
monitors = get_monitor_info()

# Ask user to select the monitor
while True:
    try:
        monitor_index = int(input(f"Enter the index of the monitor where Safari is located (0-{len(monitors)-1}): "))
        if 0 <= monitor_index < len(monitors):
            target_monitor = monitors[monitor_index]
            break
        else:
            print("Invalid monitor index. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

print(f"Selected monitor: {target_monitor}")

# Play initial beep
beep(440, 1.0)

# Open Safari with initial URL
initial_url = "https://www.example.com"
print(f"Opening Safari with URL: {initial_url}")
open_safari_with_url(initial_url)

# Wait for Safari to open and load the page
time.sleep(5)

# Ask user for click coordinates
click_x = int(input("Enter the X coordinate for the click (relative to the screenshot): "))
click_y = int(input("Enter the Y coordinate for the click (relative to the screenshot): "))

directory='/Users/macbookpro/Downloads/urban_computing/'

# Loop to take screenshots and perform click
for i in range(664,680,1):  # 4 screenshots
    try:
        # Take screenshot
        screenshot_region = (target_monitor.x + 1, target_monitor.y + 140, 1340, 870)
        print(f"Taking screenshot with region: {screenshot_region}")
        im = pyautogui.screenshot(region=screenshot_region)
        im.save(directory+f'{i}.png')
        print(f"Screenshot {i} saved")

        # Perform click
        absolute_x = target_monitor.x + 1 + click_x
        absolute_y = target_monitor.y + 140 + click_y
        click_at_position(absolute_x, absolute_y)

        # Wait before next action
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
        beep(880, 0.5)  # Error beep

# Play final beep
beep(440, 3.0, 1.0)

print("Script completed. Please check the saved screenshots and click actions.")