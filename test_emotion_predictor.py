import unittest
from my_emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_emotion_predictor(self):
        text = "I am happy"
        result = emotion_predictor(text)
        self.assertIn('emotions', result)
        self.assertIn('joy', result['emotions'])

if __name__ == '__main__':
    unittest.main()
