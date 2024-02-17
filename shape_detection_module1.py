import cv2

detected_shape = None

def detect_shapes(image):
    global detected_shape
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
            shape = "3sds"
        elif num_vertices == 4:
            shape = "4sds"
        elif num_vertices == 5:
            shape = "5sds"
        elif num_vertices == 6:
            shape = "6sds"
        else:
            shape = ""

        # Draw the shape and display it
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
        cv2.putText(image, shape, (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    return image
    
