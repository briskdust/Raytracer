FROM python:3.9.18-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY . .

CMD ["python", "main.py"]
