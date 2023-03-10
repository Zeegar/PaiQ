import RPi.GPIO as GPIO
import subprocess

# Set up GPIO pin 4 as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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
        subprocess.Popen(["python", "SendData.py"])

# Add button press event detection
GPIO.add_event_detect(4, GPIO.FALLING, callback=button_callback, bouncetime=300)

# Main loop to keep the script running
try:
    while True:
        pass

# Clean up GPIO pins when script is interrupted
except KeyboardInterrupt:
    GPIO.cleanup()