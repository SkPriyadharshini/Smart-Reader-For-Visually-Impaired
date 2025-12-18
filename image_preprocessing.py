import cv2
import numpy as np

def invert_if_white_text(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the grayscale image
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Calculate the mean pixel intensity of the thresholded image
    mean_intensity = np.mean(binary)

    # If the mean intensity is low, it means the image is predominantly dark (white text on a dark background)
    if mean_intensity < 128:
        # Invert the image to make it dark text on a white background
        img = cv2.bitwise_not(img)

    return img

# Load your image
image = cv2.imread('your_image.png')

# Process the image to invert if necessary
processed_image = invert_if_white_text(image)

# Save or display the result
cv2.imwrite('processed_image.png', processed_image)
cv2.imshow('Processed Image', processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
