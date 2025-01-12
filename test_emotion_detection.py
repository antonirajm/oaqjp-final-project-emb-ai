''' Unit test module for emotion detection '''
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        ''' Test function for emotion detector '''
        # Test case for joy
        restult_1 = emotion_detector("I am glad this happened")
        self.assertEqual(restult_1['dominant_emotion'],'joy')

        # Test case for anger
        restult_2 = emotion_detector("I am really mad about this")
        self.assertEqual(restult_2['dominant_emotion'],'anger')

        # Test case for disgust
        restult_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(restult_3['dominant_emotion'],'disgust')

        # Test case for sadness
        restult_4 = emotion_detector("I am so sad about this")
        self.assertEqual(restult_4['dominant_emotion'],'sadness')

        # Test case for fear
        restult_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(restult_5['dominant_emotion'],'fear')

# Run the tests
unittest.main()