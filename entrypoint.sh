#!/bin/bash
set -e

MODEL_NAME=$(yq e '.ollama.model' /app/config.yaml)

if [ -z "$MODEL_NAME" ]; then
    echo "Error: Could not read ollama.model from config.yaml.  Ensure 'yq' is installed and config.yaml is accessible."
    exit 1
fi

mkdir -p /root/.ollama

# Start Ollama server in the background
ollama serve &

# Wait for the Ollama server to become ready
TIMEOUT=60
START_TIME=$(date +%s)
while true; do
  if ollama list > /dev/null 2>&1; then
    echo "Ollama server is ready."
    break
  else
    CURRENT_TIME=$(date +%s)
    ELAPSED_TIME=$((CURRENT_TIME - START_TIME))
    if [[ "$ELAPSED_TIME" -gt "$TIMEOUT" ]]; then
      echo "Timeout waiting for Ollama server to start."
      exit 1
    fi
    echo "Waiting for Ollama server..."
    sleep 2
  fi
done

if ! ollama list | grep -q "$MODEL_NAME"; then
    echo "Model '$MODEL_NAME' not found.  Pulling..."
    ollama pull "$MODEL_NAME"
else
    echo "Model '$MODEL_NAME' already exists."
fi

wait