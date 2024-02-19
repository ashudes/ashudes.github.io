import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt

class ObjectDetector:
    def __init__(self):
        # Load the object detection model from TensorFlow Hub
        self.model = hub.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2')

    def load_image(self, image_path):
        # Load the image
        image_string = tf.io.read_file(image_path)
        image = tf.image.decode_jpeg(image_string, channels=3)
        # Add a batch dimension
        return tf.expand_dims(image, 0)

    def detect_objects(self, image):
        # Run the model on the image
        return self.model(image)

    def visualize_output(self, image, result):
        # Convert image from TensorFlow to a format that can be used with matplotlib
        image = image[0].numpy() / 255.0  # Convert values to [0, 1] for matplotlib

        # Get the detection boxes, classes, and scores from the model result
        boxes = result["detection_boxes"][0].numpy()
        classes = result["detection_classes"][0].numpy().astype(int)
        scores = result["detection_scores"][0].numpy()

        # Create a figure and axes
        fig, ax = plt.subplots(1)

        # Display the image
        ax.imshow(image)

        # Draw a rectangle around each detected object
        for i in range(len(boxes)):
            if scores[i] > 0.5:  # Only show detections with a confidence score > 0.5
                ymin, xmin, ymax, xmax = boxes[i]
                rect = plt.Rectangle((xmin*image.shape[1], ymin*image.shape[0]), (xmax-xmin)*image.shape[1], (ymax-ymin)*image.shape[0], fill=False, edgecolor='red', linewidth=2)
                ax.add_patch(rect)

        # Show the plot
        plt.show()

# Usage:
detector = ObjectDetector()
image_path = r'C:\Users\ahordofa\OneDrive - Chemonics\Desktop\pers\University of Essex\Module2 - OOP\Assignment2\Autonomous Car OOP\Images\ObjectDetection.jpg'
image = detector.load_image(image_path)
result = detector.detect_objects(image)
detector.visualize_output(image, result)

