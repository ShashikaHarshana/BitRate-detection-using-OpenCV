FROM python:3.9-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends libatlas-base-dev ffmpeg libsm6 libxext6 gcc python3-opencv

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your Python file into the container
COPY . .

# Upgrade pip and install the required Python packages
RUN python -m pip install pip --upgrade && pip install --index-url=https://www.piwheels.org/simple -r requirements.txt

# Run the Python file
CMD [ "python3", ",/main.py"]

# FROM python:3.9

# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt install libsm6

# RUN mkdir /app
# WORKDIR /app
# ADD . /Bitrate_Cal/
# RUN pip install pip --upgrade
# RUN pip install --no-cache-dir -r requirement.txt

# CMD ["python", "/app/app.py"]