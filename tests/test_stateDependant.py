import unittest
from unittest.mock import patch, MagicMock
import stateDependant
import gpio_utils

class TestStateDependant(unittest.TestCase):

    @patch('stateDependant.subprocess.Popen')
    def test_button_callback_start_state(self, mock_popen):
        stateDependant.current_state = stateDependant.STATE_START
        stateDependant.button_callback(4)
        mock_popen.assert_called_once_with(["edge-impulse-daemon"])
        self.assertEqual(stateDependant.current_state, stateDependant.STATE_DATA)

    @patch('stateDependant.subprocess.Popen')
    def test_button_callback_data_state(self, mock_popen):
        stateDependant.current_state = stateDependant.STATE_DATA
        stateDependant.button_callback(4)
        mock_popen.assert_called_once_with(["python3", "SendData.py"])

    @patch('gpio_utils.setup_gpio')
    def test_gpio_setup(self, mock_setup_gpio):
        stateDependant.gpio_utils.setup_gpio(4)
        mock_setup_gpio.assert_called_once_with(4)

    @patch('gpio_utils.cleanup_gpio')
    def test_gpio_cleanup(self, mock_cleanup_gpio):
        stateDependant.gpio_utils.cleanup_gpio()
        mock_cleanup_gpio.assert_called_once()

if __name__ == '__main__':
    unittest.main()
