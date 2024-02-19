# Here, I am importing the necessary classes from my 3 modules
# The LaneDetector class is responsible for detecting lanes in an image
from Module1_Lane_detection import LaneDetector
# The SensorDataProcessor class is responsible for detecting objects in an image
from Module2_Object_detection import SensorDataProcessor
# The NavigationControl class is responsible for handling navigation and control
from Module3_Navigation_Control import NavigationControl

def main():
    # Creating instances of the classes
    # This creates an instance of the LaneDetector class
    lane_detector = LaneDetector()
    # This creates an instance of the SensorDataProcessor class
    object_detector = SensorDataProcessor()
    # This creates an instance of the NavigationControl class
    navigation_control = NavigationControl()

    # Now we can call the methods of these classes
    # For example:
    # This runs the lane detection process
    lane_detector.run_lane_detection()
    # This runs the object detection process
    object_detector.run_object_detection()
    # This runs the navigation and control process
    navigation_control.run_navigation_control()

# This line ensures that the main function is only run when this script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()

