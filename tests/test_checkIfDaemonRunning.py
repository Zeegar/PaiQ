import unittest
from unittest.mock import patch, MagicMock
import checkIfDaemonRunning
import gpio_utils

class TestCheckIfDaemonRunning(unittest.TestCase):

    @patch('checkIfDaemonRunning.subprocess.Popen')
    def test_button_callback_start_state(self, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout.readline.side_effect = [
            b'Connected to wss://remote-mgmt.edgeimpulse.com\n', b''
        ]
        mock_popen.return_value = mock_process

        checkIfDaemonRunning.current_state = checkIfDaemonRunning.STATE_START
        checkIfDaemonRunning.button_callback(4)

        self.assertEqual(checkIfDaemonRunning.current_state, checkIfDaemonRunning.STATE_DATA)
        mock_popen.assert_called_once_with(["edge-impulse-daemon"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @patch('checkIfDaemonRunning.subprocess.Popen')
    def test_button_callback_data_state(self, mock_popen):
        checkIfDaemonRunning.current_state = checkIfDaemonRunning.STATE_DATA
        checkIfDaemonRunning.button_callback(4)

        mock_popen.assert_called_once_with(["python3", "SendData.py"])

    @patch('gpio_utils.setup_gpio')
    def test_gpio_setup(self, mock_setup_gpio):
        checkIfDaemonRunning.gpio_utils.setup_gpio(4)
        mock_setup_gpio.assert_called_once_with(4)

    @patch('gpio_utils.cleanup_gpio')
    def test_gpio_cleanup(self, mock_cleanup_gpio):
        checkIfDaemonRunning.gpio_utils.cleanup_gpio()
        mock_cleanup_gpio.assert_called_once()

if __name__ == '__main__':
    unittest.main()
