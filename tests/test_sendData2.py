import unittest
from unittest.mock import patch, MagicMock
import sendData2
import gpio_utils

class TestSendData2(unittest.TestCase):

    @patch('sendData2.subprocess.Popen')
    def test_start_daemon(self, mock_popen):
        mock_process = MagicMock()
        mock_process.stdout.readline.side_effect = [
            b'Connected to wss://remote-mgmt.edgeimpulse.com\n',
            b''
        ]
        mock_popen.return_value = mock_process

        sendData2.start_daemon()

        mock_popen.assert_called_once_with(["edge-impulse-daemon"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(sendData2.current_state, sendData2.STATE_DATA)

    @patch('sendData2.subprocess.Popen')
    def test_send_data(self, mock_popen):
        sendData2.send_data()
        mock_popen.assert_called_once_with(["python3", "SendData.py"])

    @patch('gpio_utils.setup_gpio')
    @patch('gpio_utils.handle_button_press')
    def test_main(self, mock_handle_button_press, mock_setup_gpio):
        with patch('sendData2.gpio_utils.cleanup_gpio') as mock_cleanup_gpio:
            with self.assertRaises(KeyboardInterrupt):
                sendData2.main()

            mock_setup_gpio.assert_called_once_with(4)
            mock_handle_button_press.assert_called_once_with(4, sendData2.button_callback)
            mock_cleanup_gpio.assert_called_once()

if __name__ == '__main__':
    unittest.main()
