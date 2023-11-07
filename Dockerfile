# Use an official Python
FROM python:3.9

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Set the working directory within the container
WORKDIR /app

# Install the 'iputils-ping' package to provide the 'ping' command
RUN apt-get update && apt-get install -y iputils-ping

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY app/ /app
COPY tests/ /app/tests/

CMD ["python", "main.py"]
