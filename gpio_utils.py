import RPi.GPIO as GPIO
import time

def setup_gpio(pin, mode=GPIO.BCM, pull_up_down=GPIO.PUD_UP):
    GPIO.setmode(mode)
    GPIO.setup(pin, GPIO.IN, pull_up_down=pull_up_down)

def handle_button_press(pin, callback, debounce_time=0.5):
    last_press_time = 0

    def button_press(channel):
        nonlocal last_press_time
        if (time.time() - last_press_time) >= debounce_time:
            callback(channel)
        last_press_time = time.time()

    GPIO.add_event_detect(pin, GPIO.FALLING, callback=button_press, bouncetime=int(debounce_time * 1000))

def cleanup_gpio():
    GPIO.cleanup()
