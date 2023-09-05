import cv2

# Load the input image
input_image = cv2.imread("input.jpg")
# Convert the image to grayscale
grayscale_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
# Apply different colormaps
colormap_jet = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_JET)
colormap_hot = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_HOT)
colormap_autumn = cv2.applyColorMap(grayscale_image, cv2.COLORMAP_AUTUMN)

# Display the original grayscale image and the colorized versions
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imshow("Jet Colormap", colormap_jet)
cv2.imshow("Hot Colormap", colormap_hot)
cv2.imshow("Autumn Colormap", colormap_autumn)
adaptive_threshold = cv2.adaptiveThreshold(
    grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

# Save the thresholded image as "output_thresholded.jpg"
cv2.imwrite("output_thresholded.jpg", adaptive_threshold)

print("Thresholded image saved as 'output_thresholded.jpg'.")

cv2.waitKey(0)
cv2.destroyAllWindows()