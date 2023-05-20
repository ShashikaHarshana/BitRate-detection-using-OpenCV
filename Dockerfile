FROM arm32v7/python:latest

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev

# Set the working directory
WORKDIR /app

# Copy your Python file into the container
COPY main.py .

# Install the required Python packages
RUN pip install opencv_python-4.5.3.56-cp39-cp39-linux_armv7l.whl

# Run the Python file
CMD ["python", "main.py"]

# FROM python:3.9

# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt install libsm6

# RUN mkdir /app
# WORKDIR /app
# ADD . /Bitrate_Cal/
# RUN pip install pip --upgrade
# RUN pip install --no-cache-dir -r requirement.txt

# CMD ["python", "/app/app.py"]