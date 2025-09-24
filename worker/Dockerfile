FROM python:3.11-slim
WORKDIR /worker
RUN apt-get update && apt-get install -y ffmpeg build-essential git && rm -rf /var/lib/apt/lists/*

COPY worker/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY worker /worker
CMD ["python", "worker.py"]
