import pyautogui
import time
from PIL import Image
import os

def click_region(x, y):
    pyautogui.click(x, y)

def capture_custom_window(left, top, width, height):
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def save_screenshot(screenshot, filename):
    screenshot.save(filename)

def main():
    # Configuration
    click_x, click_y = 100, 100  # Adjust these coordinates to match your desired click location
    capture_left, capture_top = 200, 200  # Adjust these coordinates for your custom window
    capture_width, capture_height = 800, 600  # Adjust the size of your custom window
    save_directory = "/Users/macbookpro/Downloads"  # Replace with your desired save location
    num_iterations = 5  # Number of times to repeat the process
    delay_between_iterations = 5  # Delay in seconds between iterations

    # Create save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    for i in range(num_iterations):
        # Click the specified region
        click_region(click_x, click_y)
        
        # Wait for any page load or changes
        time.sleep(2)
        
        # Capture the custom window
        screenshot = capture_custom_window(capture_left, capture_top, capture_width, capture_height)
        
        # Save the screenshot
        filename = os.path.join(save_directory, f"screenshot_{i+1}.png")
        save_screenshot(screenshot, filename)
        
        print(f"Screenshot {i+1} saved: {filename}")
        
        # Wait before the next iteration
        time.sleep(delay_between_iterations)

if __name__ == "__main__":
    main()