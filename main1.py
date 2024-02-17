import cv2
from library.shape_detection_module1 import detect_shapes, detected_shape

def main():
    # Open a connection to the webcam (0 represents the default camera)
    cap = cv2.VideoCapture(1)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Perform shape detection on the frame
        result_frame = detect_shapes(frame)

        # Access the detected shape from the global variable
        print(f"Detected Shape: {detected_shape}")

        # Display the resulting frame
        cv2.imshow("Shape Detection", result_frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
