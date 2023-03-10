import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# initialize variables
button_pressed_count = 0
button_last_state = False
button_last_time = 0
daemon_running = False

def debounce(channel):
    reading = GPIO.input(channel)
    time.sleep(0.05)
    reading = GPIO.input(channel)
    return reading

while True:
    # check for button press
    button_current_state = GPIO.input(4)

    if button_current_state != button_last_state:
        if button_current_state == False:
            if debounce(4) == GPIO.LOW:
                button_pressed_count += 1
                print("Button pressed {} times".format(button_pressed_count))

                # if button pressed 3 times in succession and daemon is not running, start the daemon and set the button count to 1
                if button_pressed_count == 3 and not daemon_running:
                    current_time = time.time()
                    if current_time - button_last_time < 1:  # check if the 3 button presses were in succession
                        print("Running edge-impulse-daemon command...")
                        subprocess.Popen(["edge-impulse-daemon"])
                        daemon_running = True
                        button_pressed_count = 1
                    button_last_time = current_time
                else:
                    button_pressed_count = 0  # reset button pressed count if conditions not met
                
        button_last_state = button_current_state


    # check for single button press
    if button_pressed_count == 1 and daemon_running:
        if debounce(4) == GPIO.LOW:
            print("Running SendData.py command...")
            subprocess.call(["python3", "SendData.py"])
            daemon_running = False  # reset daemon_running flag
            button_pressed_count = 0

    # add a small delay to avoid high CPU usage
    time.sleep(0.1)