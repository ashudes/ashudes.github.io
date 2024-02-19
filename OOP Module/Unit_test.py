import unittest
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from Module1_Lane_detection import LaneDetector
from Module2_Object_detection import visualize_output

class TestLaneDetector(unittest.TestCase):
    def setUp(self):
        self.detector = LaneDetector()
        self.test_image_path = r"C:\Users\ahordofa\OneDrive - Chemonics\Desktop\pers\University of Essex\Module2 - OOP\Assignment2\Autonomous Car OOP\Images\LaneImage1.jpg"

    def test_read_image(self):
        image = self.detector.read_image(self.test_image_path)
        self.assertIsInstance(image, np.ndarray)  # Check that the result is a numpy array

    def test_preprocess(self):
        image = self.detector.read_image(self.test_image_path)
        preprocessed_image = self.detector.preprocess(image)
        self.assertIsInstance(preprocessed_image, np.ndarray)  # Check that the result is a numpy array

class TestObjectDetection(unittest.TestCase):
    def setUp(self):
        self.test_image_path = r"C:\Users\ahordofa\OneDrive - Chemonics\Desktop\pers\University of Essex\Module2 - OOP\Assignment2\Autonomous Car OOP\Images\ObjectDetection.jpg"
        image_string = tf.io.read_file(self.test_image_path)
        self.image = tf.image.decode_jpeg(image_string, channels=3)
        self.image = tf.expand_dims(self.image, 0)

        # Load the object detection model from TensorFlow Hub
        model = hub.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2')
        self.result = model(self.image)

    def test_visualize_output(self):
        # Since visualize_output function shows a plot which doesn't return a value,
        # we can't assert the result. But we can check if the function runs without throwing an error.
        try:
            visualize_output(self.image, self.result)
            error = False
        except:
            error = True
        self.assertFalse(error)

if __name__ == '__main__':
    unittest.main()
