import cv2

# Load the image
image = cv2.imread('lion king.jpg')

# Convert the image to greyscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resive the grayscaled image
resized = cv2.resize(grey, (224, 224))

# Display the modified image
cv2.imshow('Processed Image', resized)

key = cv2.waitKey(0)  # Wait for a key press

# Ckecks if the S key was pressed
if key == ord('s'):
    # Save the processed image when s is pressed
    cv2.imwrite('resized_grey_image.jpg', resized)
    print('Image saved as resized_grey_image.jpg')
else:
    print('Image not saved.') 

cv2.destroyAllWindows()

# Print the dimensions of image (height, width, channels)
print(f"Image Dimensions: {resized.shape}")