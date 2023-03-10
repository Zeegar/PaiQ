import RPi.GPIO as GPIO
import subprocess
import time

# Set up GPIO pin 4 as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define state variables
STATE_START = 1
STATE_DATA = 2
current_state = STATE_START

# Define global flag variable for daemon startup
is_daemon_started = False

# Define function to handle button press
def button_callback(channel):
    global current_state
    global is_daemon_started
    if current_state == STATE_START and not is_daemon_started:
        process = subprocess.Popen(["edge-impulse-daemon"], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        if b"build your machine learning model!" in output:
            is_daemon_started = True
            current_state = STATE_DATA
    elif current_state == STATE_DATA:
        subprocess.Popen(["python3", "SendData.py"])


# Add button press event detection
GPIO.add_event_detect(4, GPIO.FALLING, callback=button_callback, bouncetime=300)

# Main loop to keep the script running
try:
    while True:
        if is_daemon_started:
            time.sleep(10) # Wait for the daemon to start up
            is_daemon_started = False # Reset the flag variable after timeout
except KeyboardInterrupt:
    GPIO.cleanup()