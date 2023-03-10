import RPi.GPIO as GPIO
import subprocess

# Set up GPIO pin 4 as input
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define state variables
STATE_START = 1
STATE_DATA = 2
current_state = STATE_START


def main():
    # Add button press event detection
    GPIO.add_event_detect(4, GPIO.FALLING, callback=button_callback, bouncetime=300)

    # Main loop to keep the script running
    try:
        while True:
            pass

    # Clean up GPIO pins when script is interrupted
    except KeyboardInterrupt:
        GPIO.cleanup()


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
