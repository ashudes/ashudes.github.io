import cv2
import numpy as np

class LaneDetector:
    def __init__(self):
        pass

    def read_image(self, image_path):
        image = cv2.imread(image_path)
        return image

    def preprocess(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        return blur

    def detect_edges(self, image):
        edges = cv2.Canny(image, 50, 150)
        return edges

    def define_roi(self, image):
        height, width = image.shape[:2]
        mask = np.zeros_like(image)
        vertices = np.array([[(0.6, height), (width * 0.5, height * 0.3), (width, height)]], dtype=np.int32)
        cv2.fillPoly(mask, vertices, 255)
        masked_image = cv2.bitwise_and(image, mask)
        return masked_image

    def detect_lanes(self, image):
        lines = cv2.HoughLinesP(image, rho=1, theta=np.pi/180, threshold=50, minLineLength=100, maxLineGap=250)
        return lines

    def draw_lanes(self, image, lines):
        line_image = np.zeros_like(image)
        if lines is not None:
            for line in lines:
                for x1, y1, x2, y2 in line:
                    cv2.line(line_image, (x1, y1), (x2, y2), (255, 255, 255), 10)
        return line_image

if __name__ == "__main__":
    detector = LaneDetector()
    image_path = r"C:\Users\ahordofa\OneDrive - Chemonics\Desktop\pers\University of Essex\Module2 - OOP\Assignment2\Autonomous Car OOP\Images\LaneImage1.jpg"
    image = detector.read_image(image_path)
    
    # Preprocess the image
    preprocessed_image = detector.preprocess(image)
    cv2.imshow("Preprocessed Image", preprocessed_image)
    cv2.waitKey(0)

    # Detect edges
    edges = detector.detect_edges(preprocessed_image)
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)

    # Define region of interest
    roi = detector.define_roi(edges)
    cv2.imshow("Region of Interest", roi)
    cv2.waitKey(0)

    # Detect lanes
    lanes = detector.detect_lanes(roi)

    # Draw lanes
    lane_image = detector.draw_lanes(image, lanes)
    cv2.imshow("Lane Image", lane_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
