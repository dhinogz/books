# Pull base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory 
WORKDIR /projects

# Install dependencies
COPY Pipfile Pipfile.lock /projects/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /projects/