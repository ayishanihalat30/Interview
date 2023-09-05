import cv2
# To load an image
# image=cv2.imread('image.jpg')
# # Display it in a window
# cv2.imshow("image",image)
# #resize images
# resize_image=cv2.resize(image, (500, 500))
# cv2.imshow("resizeimage",resize_image)
# key=cv2.waitKey(0)
# if key=='q':  # Check if any key is pressed
#         cv2.destroyAllWindows()
# for implementing multiple images one by one:
import cv2

# List of image file paths
image_paths = ["image.jpg", "image1.jpeg", "image2.jpg"]

# Loop through the list of image paths
for image_path in image_paths:
    # Load an image from the current file path
    image = cv2.imread(image_path)



    # Display the image in a window
    cv2.imshow("Loaded Image", image)

    # Dynamically resize the window (adjust these values as needed)
    width, height = 800, 600
    cv2.resizeWindow("Loaded Image", width, height)

    # Wait for a key press or a specified delay
    key = cv2.waitKey(1000)

    # Close the window if any key is pressed (or after the specified delay)
    if key != -1:
        cv2.destroyAllWindows()
