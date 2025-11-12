# Stage 1: build dependencies and collect app
FROM python:3.13-slim AS builder

WORKDIR /app

# Install dependencies into a separate prefix
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

# Copy source code
COPY . .

# Stage 2: minimal runtime image
FROM python:3.13-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY --from=builder /app /app

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "run.py"]