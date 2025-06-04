# Base Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all files from current dir to container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run your script
CMD ["python", "run.py"]
