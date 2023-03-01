FROM python:3.10-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p /opt

WORKDIR /opt

COPY . /opt

ENTRYPOINT ["python", "/opt/server.py"]
CMD ["--port", "8080"]

HEALTHCHECK --interval=10s --timeout=3s \
    CMD curl http://localhost:8080
