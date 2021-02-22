FROM python:3.9-buster
RUN apt-get update && apt-get install -y ffmpeg
WORKDIR /app
CMD ["/app/fry.py"]