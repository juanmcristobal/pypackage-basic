# Use the official Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory inside the container
WORKDIR /app

# Update the package list and install essential packages
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    && apt-get clean

# Add the deadsnakes PPA for multiple Python versions
RUN add-apt-repository ppa:deadsnakes/ppa

# Update the package list again to include the new repository
RUN apt-get update

# Install Python versions 3.7 to 3.11
RUN apt-get install -y \
    python3.7 \
    python3.8 \
    python3.9 \
    python3.10 \
    python3.11 \
    python3.12 \
    && apt-get clean

# Install pip for each Python version
RUN apt-get install -y \
    python3.7-distutils \
    python3.8-distutils \
    python3.9-distutils \
    python3.10-distutils \
    python3.11-distutils \
    python3.12-distutils \
    && apt-get clean

# Set Python 3.9 as the default python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1

# Install pip for Python 3.9
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.9 get-pip.py

# Install tox for Python 3
RUN python3 -m pip install tox

# Set the default command to run tox
CMD ["tox"]
