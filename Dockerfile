FROM python:3.13-slim

WORKDIR /app
COPY pyproject.toml README.md LICENSE ./
COPY skilldx ./skilldx
RUN pip install --no-cache-dir .

WORKDIR /work
ENTRYPOINT ["skilldx"]
CMD ["--help"]
