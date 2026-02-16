# FROM nvidia/cuda:12.8.0-runtime-ubuntu22.04

# # Set environment variables
# ENV DEBIAN_FRONTEND=noninteractive
# ENV PYTHONUNBUFFERED=1
# ENV CUDA_HOME=/usr/local/cuda

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     python3-dev \
#     git \
#     wget \
#     curl \
#     && rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /app

# COPY . .

# # RUN pip install -e .

# RUN pip install -r sam3WebAPP/requirements.txt

# # Expose port 5000
# EXPOSE 5000

# # Set the default command
# # Note: the module path must not have a leading space
# # gunicorn webapp.inference:app -c webapp/gunicorn.conf.py
# # CMD ["gunicorn", "webapp.inference:app", "-c", "webapp/gunicorn.conf.py"]

# # for testing purposes
# CMD ["python3", "sam3WebAPP/main.py"]

# docker script for containerizing the app

# base image
FROM python:3.12-slim

# set working directory
WORKDIR /app

# copy the files
# COPY test.py test.py
COPY main.py .
COPY requirements.txt .
COPY .env .

# install dependencies 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python", "main.py"]
