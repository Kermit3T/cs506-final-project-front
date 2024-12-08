# Detect operating system
ifeq ($(OS),Windows_NT)
	PYTHON_CMD = python
	PIP_CMD = pip
	VENV_DIR = venv
	ACTIVATE_CMD = $(VENV_DIR)/Scripts/activate
	SEP = &&
else
	PYTHON_CMD = python3
	PIP_CMD = pip3
	VENV_DIR = venv
	ACTIVATE_CMD = . $(VENV_DIR)/bin/activate
	SEP = ;
endif

# Default target
.PHONY: all
all: setup run

# Setup both frontend and backend
.PHONY: setup
setup: setup-frontend setup-backend

# Frontend setup
.PHONY: setup-frontend
setup-frontend:
	npm install

# Backend setup
.PHONY: setup-backend
setup-backend:
	$(PYTHON_CMD) -m venv $(VENV_DIR)
	$(ACTIVATE_CMD) $(SEP) $(PIP_CMD) install --upgrade pip $(SEP) $(PIP_CMD) install -r requirements.txt

# Run both frontend and backend
.PHONY: run
run:
	@echo "Starting the application..."
ifeq ($(OS),Windows_NT)
	start /B npm run dev $(SEP) start /B $(ACTIVATE_CMD) $(SEP) uvicorn api.app:app --reload
else
	npm run dev & $(ACTIVATE_CMD) $(SEP) uvicorn api.app:app --reload
endif

# Clean up
.PHONY: clean
clean:
ifeq ($(OS),Windows_NT)
	if exist $(VENV_DIR) rmdir /s /q $(VENV_DIR)
	if exist node_modules rmdir /s /q node_modules
else
	rm -rf $(VENV_DIR)
	rm -rf node_modules
endif

# Install model (assuming it's downloaded separately due to size)
.PHONY: install-model
install-model:
	@echo "Checking for model directory..."
ifeq ($(OS),Windows_NT)
	if not exist "api\models" mkdir "api\models"
else
	mkdir -p api/models
endif
	@echo "Please place the breast_cancer_cnn_model.keras file in the api/models directory"

# Help command
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make setup         - Set up both frontend and backend dependencies"
	@echo "  make run          - Run both frontend and backend servers"
	@echo "  make clean        - Remove virtual environment and node_modules"
	@echo "  make install-model - Set up model directory (model file needs to be added manually)"
	@echo "  make help         - Show this help message"