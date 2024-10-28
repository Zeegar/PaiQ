import unittest
from unittest.mock import patch, MagicMock
import SendData

class TestSendData(unittest.TestCase):

    @patch('http.client.HTTPSConnection')
    def test_send_data(self, MockHTTPSConnection):
        mock_conn = MockHTTPSConnection.return_value
        mock_conn.getresponse.return_value.read.return_value.decode.return_value = 'response data'

        SendData.main()

        MockHTTPSConnection.assert_called_with("studio.edgeimpulse.com")
        mock_conn.request.assert_called_with(
            "POST",
            f"/v1/api/{SendData.project_ID}/device/{SendData.device_ID}/start-sampling",
            SendData.payload,
            SendData.headers
        )
        mock_conn.getresponse.assert_called_once()

if __name__ == '__main__':
    unittest.main()
