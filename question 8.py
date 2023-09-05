import cv2

# Load the input image
input_image = cv2.imread("input.jpg")


# Experiment with different kernel sizes and sigma values
kernel_sizes = [3, 5, 7]
sigma_values = [0.5, 1.0, 2.0]

for kernel_size in kernel_sizes:
    for sigma in sigma_values:
        # Apply Gaussian blur
        blurred_image = cv2.GaussianBlur(input_image, (kernel_size, kernel_size), sigma)

        # Generate a meaningful filename based on kernel size and sigma
        filename = f"blurred_kernel{kernel_size}_sigma{sigma}.jpg"

        # Save the blurred image with the meaningful filename
        cv2.imwrite(filename, blurred_image)

        print(f"Blurred image saved as '{filename}'.")

print("Blurring experiments completed.")
