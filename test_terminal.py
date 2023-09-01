import unittest
import terminal


term = terminal.Terminal()
class TestTerminal(unittest.TestCase):


    def test_show_help(self):
        output = term.show_help()
        self.assertIsNone(output)

    def test_show_dir(self):
        output = term.show_dir()
        self.assertIsNone(output)


if __name__ == "__main__":
    unittest.main()