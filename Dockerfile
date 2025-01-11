FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 python \
  && useradd --uid 1000 --gid python --shell /bin/bash --create-home python

EXPOSE 9093

WORKDIR /app

RUN mkdir -p /app/static /app/static-cdn/ /app/media/

COPY requirements.txt ./
COPY .env ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh \
    && chown -R python:python /app

USER python

ENTRYPOINT ["/app/entrypoint.sh"]
