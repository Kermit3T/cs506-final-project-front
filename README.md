# Cancer Cell Detection Web Application

## Overview
This web application provides an interface for analyzing microscopy images to detect and classify cancer cells. The application uses a TensorFlow model to classify cells into three categories: High, Low, and Stroma. Users can upload and crop images, which are then analyzed by the model.

## Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm (usually comes with Node.js)
- Git

## Installation

### Setting Up the Project Using Make (Recommended)
```bash
# Clone the repository
git clone https://github.com/Kermit3T/cs506-final-project-front
cd your-repo-name

# Install all dependencies and set up environment
make setup

# Download the model
make install-model

# Run both frontend and backend
make run
The frontend will run on http://localhost:5173
The backend will run on http://localhost:8000
Available make commands:

make setup - Set up frontend and backend dependencies
make run - Start both servers
make clean - Remove virtual environment and node_modules
make install-model - Download model file
make help - Show all available commands
```

### Setting Up the Project Manually

### 1. Clone the Repository
```bash
git clone https://github.com/Kermit3T/cs506-final-project-front
cd your-repo-name
```

### 2. Set Up Python Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies
```bash
pip install tensorflow fastapi uvicorn python-multipart pillow numpy
```

### 4. Install Node.js Dependencies
```bash
npm install
```

### 5. Model Setup
Ensure the model file is in the correct location:
```
api/models/breast_cancer_cnn_model (1).keras
```

## Running the Application

### 1. Start the Backend Server
In one terminal window (with virtual environment activated):
```bash
# Windows
.\venv\Scripts\activate
uvicorn api.app:app --reload

# Mac/Linux
source venv/bin/activate
uvicorn api.app:app --reload
```
The backend will run on http://localhost:8000

### 2. Start the Frontend Server
In a new terminal window:
```bash
npm run dev
```
The frontend will run on http://localhost:5173

## Usage
1. Open http://localhost:5173 in your web browser
2. Click the upload box to select an image (minimum size 244x244 pixels)
3. Use the cropping tool to select the area for analysis
4. Click "Crop Image" and then "Test Image"
5. View the analysis results, including:
   - Classification
   - Confidence score
   - Detailed probability breakdown for each class

## Troubleshooting

### Common Issues and Solutions

1. **Backend Won't Start**
   - Ensure Python virtual environment is activated
   - Check if port 8000 is available
   - Verify model file exists in correct location

2. **Frontend Won't Start**
   - Run `npm install` to ensure all dependencies are installed
   - Check if port 5173 is available
   - Clear npm cache with `npm cache clean --force`

3. **Image Upload Issues**
   - Ensure image meets minimum size requirements (244x244)
   - Check browser console for specific error messages
   - Verify file format is supported (JPG, PNG)

4. **Analysis Fails**
   - Check backend console for error messages
   - Verify backend server is running
   - Ensure image is properly cropped before analysis

### Still Having Issues?
Create an issue on the GitHub repository with:
- Steps to reproduce the problem
- Error messages
- Screenshots if applicable
- Your system information (OS, Python version, Node.js version)

## Important Notes
- This tool is for research and preliminary screening purposes only
- Not intended for medical diagnosis
- Always consult healthcare professionals for medical advice
