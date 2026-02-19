FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Only copy test file (CI principle)
COPY test.py .

# Run CI test
CMD ["python", "test.py"]
