import cv2

# Load the input image
input_image = cv2.imread("input.jpg")


# Get the dimensions of the input image
height, width, _ = input_image.shape

# Calculate the size of the central square region
size = min(height, width)

# Calculate the coordinates for cropping the central square
x1 = (width - size) // 2
x2 = x1 + size
y1 = (height - size) // 2
y2 = y1 + size

# Crop the central square region
cropped_image = input_image[y1:y2, x1:x2]

# Choose a new size for resizing (e.g., 200x200 pixels)
new_size = (200, 200)

# Resize the cropped image to the new size
resized_image = cv2.resize(cropped_image, new_size)

# Save the resized image as "output_resized.jpg"
cv2.imwrite("output_resized.jpg", resized_image)

print("Resized image saved as 'output_resized.jpg'.")
