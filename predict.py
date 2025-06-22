import numpy as np

import cv2

from tensorflow.keras.models import load_model



# Updated model_predict_fc function for multi-class classification

def model_predict_fc(image_path, model):

    # Preprocessing and model prediction for fingerprint classification

    image = preprocess_image(image_path)

    if image is None:

        print("Error: Image preprocessing failed.")

        return None

    

    prediction = model.predict(image)  # Model will return probability distributions for each class

    predicted_class = np.argmax(prediction, axis=1)[0]  # Get the class with the highest probability

    

    return predicted_class



# Preprocessing the image for model input

def preprocess_image(image_path, target_size=(32, 32)):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if image is None:

        return None

    image = cv2.resize(image, target_size)

    image = image.astype('float32') / 255.0

    image = np.expand_dims(image, axis=(0, -1))  # Shape: (1, 32, 32, 1)

    return image



# Prediction function for returning blood group based on class label

def predict_image(model, image_path):

    image = preprocess_image(image_path)

    if image is None:

        return None

    predictions = model.predict(image)  # Predicts the probabilities for each class

    predicted_class = np.argmax(predictions, axis=1)[0]  # Get the class with the highest probability

    

    # Map predicted class index to blood group label (update this list if more groups exist)

    blood_groups = ['A+','A-','B+', 'B-','AB+', 'AB-','O+', 'O-']  # Example, adjust for your number of classes

    predicted_blood_group = blood_groups[predicted_class]

    

    return predicted_blood_group