import subprocess
import gpio_utils

# Set up GPIO pin 4 as input
gpio_utils.setup_gpio(4)

# Define state variables
STATE_START = 1
STATE_DATA = 2
current_state = STATE_START

# Define function to handle button press
def button_callback(channel):
    global current_state
    if current_state == STATE_START:
        subprocess.Popen(["edge-impulse-daemon"])
        current_state = STATE_DATA
    elif current_state == STATE_DATA:
        subprocess.Popen(["python3", "SendData.py"])

# Add button press event detection
gpio_utils.handle_button_press(4, button_callback)

# Main loop to keep the script running
try:
    while True:
        pass

# Clean up GPIO pins when script is interrupted
except KeyboardInterrupt:
    gpio_utils.cleanup_gpio()
