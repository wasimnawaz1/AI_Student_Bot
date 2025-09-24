FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y ffmpeg build-essential git && rm -rf /var/lib/apt/lists/*

COPY web/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY web/app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
