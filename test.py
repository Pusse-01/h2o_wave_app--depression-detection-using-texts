import unittest
from utils.predictor import predict


class TestPrediction(unittest.TestCase):
    def test_list_int(self):
        """
        Test the predicted label
        """
        test_cases = 'I need a break'
        result = predict(test_cases)
        self.assertEqual(result, 'Depressive')

if __name__ == '__main__':
    unittest.main()
