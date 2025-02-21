FROM ollama/ollama:latest

# Install yq
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/bin/yq && chmod +x /usr/bin/yq

COPY config/config.yaml /app/config.yaml

COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

WORKDIR /app