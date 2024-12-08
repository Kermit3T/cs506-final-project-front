# api/app.py
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import os
import tensorflow as tf

app = FastAPI(title="Cancer Cell Detection API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model at startup
MODEL_PATH = os.path.join('api', 'models', 'breast_cancer_cnn_model (1).keras')
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    model = None

# Class labels from the notebook
CLASS_LABELS = ['High', 'Low', 'Stroma']

async def preprocess_image(image_file: UploadFile):
    """
    Preprocess the uploaded image according to model requirements.
    Args:
        image_file: UploadFile object containing the image
    Returns:
        numpy array of shape (1, 224, 224, 3) ready for model prediction
    """
    try:
        # Read the image file
        image_data = await image_file.read()
        img = Image.open(io.BytesIO(image_data))

        # Convert to RGB if needed
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to target size
        target_size = (224, 224)
        img = img.resize(target_size)

        # Convert to numpy array and normalize
        img_array = np.array(img) / 255.0

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        return img_array

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image processing failed: {str(e)}")

@app.post("/api/analyze")
async def analyze_image(file: UploadFile):
    """
    Endpoint to analyze cell images for cancer detection.
    """
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Validate file type
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:
        # Preprocess the image
        processed_image = await preprocess_image(file)

        # Make prediction
        predictions = model.predict(processed_image)
        
        # Get the predicted class and confidence
        predicted_class_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class_idx])
        classification = CLASS_LABELS[predicted_class_idx]

        # Prepare detailed results
        all_confidences = {
            label: float(conf) 
            for label, conf in zip(CLASS_LABELS, predictions[0])
        }

        result = {
            "classification": classification,
            "confidence": confidence,
            "details": {
                "class_probabilities": all_confidences,
                "message": f"Image classified as {classification} with {confidence*100:.2f}% confidence"
            }
        }

        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/api/health")
async def health_check():
    """
    Health check endpoint that also verifies model status.
    """
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "available_classes": CLASS_LABELS
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)