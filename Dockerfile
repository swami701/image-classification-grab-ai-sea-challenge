FROM python:2.7

# Create app directory
RUN mkdir -p /app
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "start.py"]
