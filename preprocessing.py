import cv2

import numpy as np



def preprocess_image(image_path, target_size=(32, 32)):

    try:

        # Load the image in grayscale (still single channel)

        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:

            print(f"Error: Unable to load image at path: {image_path}")

            return None

        

        # Resize the image to 32x32 (the input size expected by LeNet)

        image = cv2.resize(image, target_size)

        

        # Normalize the image (scale pixel values to the range [0, 1])

        image = image.astype('float32') / 255.0

        

        # Reshape the image to match the model input format (batch_size, height, width, channels)

        image = np.expand_dims(image, axis=(0, -1))  # Shape: (1, 32, 32, 1)

        

        return image

    

    except Exception as e:

        print(f"Exception during preprocessing image {image_path}: {e}")

        return None