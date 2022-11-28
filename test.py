import unittest
from utils.predictor import predict


class TestPrediction(unittest.TestCase):
    def test_list_int(self):
        """
        Test the predicted label
        """
        test_cases = ['I need a break']
        labels = ['Depressive']
        for i in range(len(test_cases)):
            result, tips = predict(test_cases[i])
            self.assertEqual(result, labels[i])

if __name__ == '__main__':
    unittest.main()
