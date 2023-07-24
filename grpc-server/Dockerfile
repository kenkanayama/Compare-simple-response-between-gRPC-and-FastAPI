# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Install watchdog for auto-reload
RUN pip install watchdog[watchmedo]

CMD chmod +x ./run.sh && ./run.sh