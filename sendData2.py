import RPi.GPIO as GPIO
import subprocess
import gpio_utils

# Set up GPIO pin 4 as input
gpio_utils.setup_gpio(4)

# Define state variables
STATE_START = 1
STATE_DATA = 2
current_state = STATE_START


def main():
    # Add button press event detection
    gpio_utils.handle_button_press(4, button_callback)

    # Main loop to keep the script running
    try:
        while True:
            pass

    # Clean up GPIO pins when script is interrupted
    except KeyboardInterrupt:
        gpio_utils.cleanup_gpio()


def button_callback(channel):
    global current_state
    if current_state == STATE_START:
        start_daemon()
        current_state = STATE_DATA
    elif current_state == STATE_DATA:
        send_data()


def start_daemon():
    process = subprocess.Popen(["edge-impulse-daemon"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if "Connected to wss://remote-mgmt.edgeimpulse.com" in output.decode("utf-8"):
            break
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()


def send_data():
    subprocess.Popen(["python3", "SendData.py"])


if __name__ == "__main__":
    main()
