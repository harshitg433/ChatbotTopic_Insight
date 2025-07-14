# backend/Dockerfile
FROM python:3.11-slim-buster
WORKDIR /app
# Copy only requirements first to leverage Docker cache
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the backend application code
COPY backend/ /app/
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]