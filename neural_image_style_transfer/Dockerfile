FROM python:3.8-slim
COPY requirements.txt ./


# Below is the installation for python slim, which is 1GB smaller than the normal installation
RUN apt-get update && \
    apt-get install -y \
        build-essential \
        make \
        gcc \
    && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 \
    && pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]