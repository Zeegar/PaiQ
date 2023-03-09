import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# initialize variables
button_pressed_count = 0
button_last_state = False
cli_command_run = False

while True:
    # check for button press
    button_current_state = GPIO.input(4)

    if button_current_state != button_last_state:
        if button_current_state == False:
            button_pressed_count += 1
            print("Button pressed {} times".format(button_pressed_count))

            # if button pressed 3 times, run the CLI command
            if button_pressed_count == 3:
                print("Running edge-impulse-daemon command...")
                subprocess.call(["edge-impulse-daemon"])
                cli_command_run = True
                button_pressed_count = 0
                
        button_last_state = button_current_state
    else:
        print("Button not pressed")

    # check for single button press
    if button_pressed_count == 1 and cli_command_run:
        print("Running SendData.py command...")
        subprocess.call(["python3", "SendData.py"])
        button_pressed_count = 0

    # add a small delay to avoid high CPU usage
    time.sleep(0.1)