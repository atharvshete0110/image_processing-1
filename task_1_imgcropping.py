
import cv2
import numpy as np

# Read the image
image = cv2.imread('C:/Users/asus/Downloads/Task_1.jpg')

# Create the window named 'Cropping Image'
cv2.namedWindow('Cropping Image')
drawing_image = image.copy()
insigths_image = image.copy()

# Define a callback function for mouse events
def mouse_event(event, x, y, flags, param):
    global starting_point, ending_point, drawing_image

    if event == cv2.EVENT_LBUTTONDOWN:
        # Record the starting point of the rectangle
        starting_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if starting_point:
            # Update the drawing image with the temporary rectangle
            cv2.rectangle(drawing_image, starting_point, (x, y), (0, 255, 0), 2)
            cv2.imshow('Cropping Image', drawing_image)

    elif event == cv2.EVENT_LBUTTONUP:
        # Record the ending point of the rectangle
        ending_point = (x, y)

        # Crop the image based on the selected rectangle
        cropped_image = image[starting_point[1]:ending_point[1], starting_point[0]:ending_point[0]]
        print(cropped_image)

        # Save the cropped image
        cv2.imwrite('task_1_cropped.jpg', cropped_image)
        # cv2.imwrite('task_1_insights')

        # Draw the rectangular box and mention its top left and bottom right point on a new image
        insights_image = np.copy(image)
        cv2.rectangle(insights_image, starting_point, ending_point, (0, 0, 255), 2)
        cv2.putText(insights_image, f"Top Left: {starting_point}", (starting_point[0] + 10, starting_point[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        cv2.putText(insights_image, f"Bottom Right: {ending_point}", (ending_point[0] + 10, ending_point[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Save the insights imageo
        cv2.imwrite('Task_1_insights.jpg', insights_image)

        # Reset the drawing image and variables for the next rectangle
        drawing_image = image.copy()
        starting_point = None
        ending_point = None

# Set the mouse callback function
cv2.setMouseCallback('Cropping Image', mouse_event)

# Display the image and wait for a mouse event
cv2.imshow('Cropping Image', image)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
