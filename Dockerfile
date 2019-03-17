# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory to /api
WORKDIR /api

# Copy the current directory contents into the container at /api
COPY . /api

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV APP_SETTINGS development

# Expose port 80
EXPOSE 80

# Run main script when the container launches
CMD ["python3", "run_app.py"]
