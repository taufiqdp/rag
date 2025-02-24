# Build stage
FROM python:3.10-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --no-warn-script-location --user -r requirements.txt

# Final stage
FROM python:3.10-slim

WORKDIR /app

ENV TRANSFORMERS_CACHE=/cache/huggingface
ENV HF_HOME=/cache/huggingface
RUN mkdir -p /cache/huggingface

COPY --from=builder /root/.local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY src/ app/

COPY config/ config/

EXPOSE 8501

CMD ["python3", "-m", "streamlit", "run", "app/main.py"]
