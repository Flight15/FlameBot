# Use an official Python image from Alpine
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN apt-get -y update && \
	apt -y install build-essential && \
	pip install --no-cache-dir -r requirements.txt

# Copy the rest of the repository contents into the container
COPY . .

# Specify the command to run when the container starts
CMD ["python", "discordbot.py"]
