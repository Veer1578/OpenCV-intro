import cv2

image = cv2.imread('lion king.jpg')

if image is None:
    print("Error: Image not found or could not be opened.")
    exit()

sizes = [[200, 200], [400, 400], [600, 600]]

for size in sizes:
    resized = cv2.resize(image, tuple(size))

    cv2.imshow('Image', resized)
    key = cv2.waitKey(0)
    if key == ord('s'):
        if size == [200, 200]:
            cv2.imwrite('resized_image_small.jpg', resized)
            print('Image saved as resized_image_small.jpg')
        elif size == [400, 400]:
            cv2.imwrite('resized_image_medium.jpg', resized)
            print('Image saved as resized_image_medium.jpg')
        else:
            cv2.imwrite('resized_image_large.jpg', resized)
            print('Image saved as resized_image_large.jpg')
    else:
        print('Image not saved.')
    print(f'Image Properties: {resized.shape}')

cv2.destroyAllWindows()

    
