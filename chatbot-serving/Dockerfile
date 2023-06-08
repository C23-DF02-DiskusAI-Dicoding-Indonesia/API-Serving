# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the working directory
COPY . .

# Expose the port that the Flask app will be listening on
EXPOSE 2000

# Run the Flask app
CMD ["python", "app.py"]
