import unittest

from chatops_assistant import get_response


class ChatOpsTests(unittest.TestCase):
    def test_help_request(self):
        response = get_response("help")
        self.assertIn("status", response)
        self.assertIn("exit", response)

    def test_status_request(self):
        response = get_response("status")
        self.assertIn("2 error(s)", response)
        self.assertIn("1 warning(s)", response)
        self.assertIn("HTTP 503 Service Unavailable", response)

    def test_unknown_request_is_rejected(self):
        response = get_response("restart production")
        self.assertIn("Request not supported", response)
        self.assertIn("No action was taken", response)


if __name__ == "__main__":
    unittest.main()
