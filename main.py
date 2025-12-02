from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import ctypes
import keyboard
import pyperclip

# Get screen resolution
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Calculate dimensions for split screen
half_width = screen_width // 2
height = screen_height

# Setup first browser instance (Left side) - Google ReCaptcha Demo
options1 = webdriver.ChromeOptions()
options1.add_argument(f"--window-size={half_width},{height}")
options1.add_argument("--window-position=0,0")
driver1 = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options1
)
driver1.get("https://www.google.com/recaptcha/api2/demo")

time.sleep(5)

# Setup second browser instance (Right side) - Google Translate
options2 = webdriver.ChromeOptions()
options2.add_argument(f"--window-size={half_width},{height}")
options2.add_argument(f"--window-position={half_width},0")
driver2 = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options2
)
driver2.get("https://translate.google.com/?sl=en&tl=fa&op=translate")

# Move to and click on a specific location (likely to focus or interact)
target_x, target_y = 65, 500
pyautogui.moveTo(target_x, target_y, duration=0.5)
pyautogui.click()

time.sleep(4)

# Find iframes in the first driver
frames = driver1.find_elements(By.TAG_NAME, "iframe")
print(f"Found {len(frames)} iframes")

# Switch to the ReCaptcha iframe and click the audio challenge button
for i, f in enumerate(frames):
    driver1.switch_to.default_content()
    driver1.switch_to.frame(f)
    try:
        audio_button = driver1.find_element(By.ID, "recaptcha-audio-button")
        audio_button.click()
        print("Audio challenge button clicked.")
        break
    except:
        continue

time.sleep(3)

# Automate mouse movements and clicks to copy/paste audio link or text
# Note: These coordinates are specific to the user's screen resolution
pyautogui.moveTo(1000, 450, duration=0.5)
pyautogui.click()
pyautogui.click()
time.sleep(1)


pyautogui.moveTo(1300, 200, duration=0.5)
time.sleep(0.5)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(200, 450, duration=0.5)
time.sleep(1)
pyautogui.click()
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1000, 450, duration=0.5)
time.sleep(4)
pyautogui.click()
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(1100, 340, duration=0.5)
pyautogui.click()
pyautogui.click()
time.sleep(0.5)

# Select all and copy
keyboard.press_and_release("ctrl+a")
time.sleep(0.2)

keyboard.press_and_release("ctrl+c")
time.sleep(0.5)

# Move to paste location
pyautogui.moveTo(300, 510, duration=0.5)
pyautogui.click()
pyautogui.click()
time.sleep(0.3)

# Paste content
keyboard.press_and_release("ctrl+v")
time.sleep(0.3)

keyboard.press_and_release("enter")


pyautogui.moveTo(80, 580, duration=0.5)
time.sleep(0.5)
pyautogui.click()

print("All tasks completed. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting program.")
