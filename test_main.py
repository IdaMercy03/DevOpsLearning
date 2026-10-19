
import unittest
from unittest.mock import patch
from app import main


class TestMain(unittest.TestCase):

    @patch("builtins.print")
    def test_main_prints_expected_messages(self, mock_print):
        main()

        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call(
            "Hello! Welcome to my DevOps learning project."
        )
        mock_print.assert_any_call(
            "My first step is creating a Python application."
        )


if __name__ == "__main__":
    unittest.main()
