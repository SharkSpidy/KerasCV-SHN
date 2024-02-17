import cv2
import numpy as np

def detect_shapes(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help the contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Get the number of vertices
        num_vertices = len(approx)

        # Identify the shape based on the number of vertices
        shape = "unknown"
        if num_vertices == 3:
            shape = "triangle"
        elif num_vertices == 4:
            shape = "rectangle"
        elif num_vertices == 5:
            shape = "pentagon"
        elif num_vertices == 6:
            shape = "hexagon"
        else:
            shape = "circle"

        # Draw the shape and display it
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        cv2.putText(image, shape, (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    return image

def main():
    # Open a connection to the webcam (0 represents the default camera)
    cap = cv2.VideoCapture(1)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Perform shape detection on the frame
        result_frame = detect_shapes(frame)

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
