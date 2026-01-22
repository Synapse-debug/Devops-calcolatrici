FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd -m appuser

COPY requirements.in .
RUN pip install --no-cache-dir -r requirements.in

COPY . .
RUN chown -R appuser:appuser /app
USER appuser

CMD ["python", "calcolatrice.py"]
