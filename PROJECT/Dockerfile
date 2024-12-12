# Use the Official Python 3.10 image as the Base Image
FROM python:3.10

# Set the Working Directory inside the container to /App
WORKDIR /App

# Copy all files from the local src directory to the Working Directory in the container
# COPY src/ .
COPY . /App
# Install the Required Python packages for the Application from Requirements.txt 
RUN pip install -r requirements.txt

# Expose port 80 to allow access to the application
EXPOSE 80

# Set the command to run Uvicorn, with app starting on port 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]