import unittest
from unittest.mock import patch, call
import gpio_utils

class TestGPIOUtils(unittest.TestCase):

    @patch('gpio_utils.GPIO')
    def test_setup_gpio(self, mock_gpio):
        gpio_utils.setup_gpio(4)
        mock_gpio.setmode.assert_called_once_with(mock_gpio.BCM)
        mock_gpio.setup.assert_called_once_with(4, mock_gpio.IN, pull_up_down=mock_gpio.PUD_UP)

    @patch('gpio_utils.GPIO')
    def test_cleanup_gpio(self, mock_gpio):
        gpio_utils.cleanup_gpio()
        mock_gpio.cleanup.assert_called_once()

    @patch('gpio_utils.GPIO')
    @patch('gpio_utils.time')
    def test_handle_button_press(self, mock_time, mock_gpio):
        callback = unittest.mock.Mock()
        gpio_utils.handle_button_press(4, callback, debounce_time=0.5)

        # Simulate button press
        mock_gpio.add_event_detect.call_args[0][2](4)
        callback.assert_called_once_with(4)

        # Simulate debounce
        callback.reset_mock()
        mock_time.time.return_value += 0.4
        mock_gpio.add_event_detect.call_args[0][2](4)
        callback.assert_not_called()

        # Simulate button press after debounce time
        mock_time.time.return_value += 0.6
        mock_gpio.add_event_detect.call_args[0][2](4)
        callback.assert_called_once_with(4)

if __name__ == '__main__':
    unittest.main()
