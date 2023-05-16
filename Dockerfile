FROM python:3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install libsm6

RUN mkdir /app
WORKDIR /app
ADD . /Bitrate_Cal/
RUN pip install pip --upgrade
RUN pip install --no-cache-dir -r requirement.txt

CMD ["python", "/app/app.py"]