import numpy as np
from PIL import Image
import io

class ImagePreprocessor:
    def __init__(self, target_size=(224, 224)):
        """
        Initialize the image preprocessor.
        Args:
            target_size (tuple): The target size for the image (width, height)
        """
        self.target_size = target_size

    def validate_image(self, image):
        """
        Validate if the image meets minimum size requirements.
        Args:
            image (PIL.Image): The image to validate
        Returns:
            bool: True if valid, False otherwise
        """
        min_size = min(self.target_size)
        return image.size[0] >= min_size and image.size[1] >= min_size

    def preprocess_image(self, image_data):
        """
        Preprocess image data for the model.
        Args:
            image_data (bytes or PIL.Image): The image to process
        Returns:
            numpy.ndarray: Preprocessed image array
        Raises:
            ValueError: If image is invalid or processing fails
        """
        try:
            # Convert bytes to PIL Image if necessary
            if isinstance(image_data, bytes):
                image = Image.open(io.BytesIO(image_data))
            else:
                image = image_data

            # Validate image
            if not self.validate_image(image):
                raise ValueError(f"Image must be at least {self.target_size[0]}x{self.target_size[1]} pixels")

            # Convert to RGB if needed
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Resize to target size
            image = image.resize(self.target_size)

            # Convert to numpy array and normalize
            img_array = np.array(image) / 255.0

            # Add batch dimension
            img_array = np.expand_dims(img_array, axis=0)

            return img_array

        except Exception as e:
            raise ValueError(f"Image preprocessing failed: {str(e)}")

    def decode_prediction(self, prediction, class_labels):
        """
        Decode model prediction into human-readable format.
        Args:
            prediction: numpy array of model predictions
            class_labels: list of class labels
        Returns:
            dict: Decoded prediction with classification and confidence
        """
        pred_idx = np.argmax(prediction[0])
        confidence = float(prediction[0][pred_idx])
        
        return {
            "classification": class_labels[pred_idx],
            "confidence": confidence,
            "details": {
                "class_probabilities": {
                    label: float(prob) 
                    for label, prob in zip(class_labels, prediction[0])
                }
            }
        }