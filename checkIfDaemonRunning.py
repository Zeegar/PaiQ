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

# Define function to handle button press
def button_callback(channel):
    global current_state
    if current_state == STATE_START:
        process = subprocess.Popen(["edge-impulse-daemon"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            output = process.stdout.readline()
            if "Connected to wss://remote-mgmt.edgeimpulse.com" in output.decode("utf-8"):
                current_state = STATE_DATA
                break
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip())
        rc = process.poll()
    elif current_state == STATE_DATA:
        subprocess.Popen(["python3", "SendData.py"])

# Add button press event detection with debounce
last_press_time = 0
debounce_time = 0.5 # in seconds
def button_press(channel):
    global last_press_time
    if (time.time() - last_press_time) >= debounce_time:
        button_callback(channel)
    last_press_time = time.time()
GPIO.add_event_detect(4, GPIO.FALLING, callback=button_press, bouncetime=300)

# Main loop to keep the script running
try:
    while True:
        pass

# Clean up GPIO pins when script is interrupted
except KeyboardInterrupt:
    GPIO.cleanup()
