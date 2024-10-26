# Selecting Python 3.10.10
FROM python:3.10.10

# Environment variable sending output directly to terminal
ENV PYTHONUNBUFFERED 1

# Creating the container root directory for DogAPI
RUN mkdir /dogapi

# Setting the container's working directory to dogapi for DogAPI
WORKDIR /dogapi

# Installing and running the requirements file to satisfy all dependencies
COPY requirements.txt /dogapi/
RUN pip install -r requirements.txt

# Populating the container with the contents of the root directory (dogapi).
COPY . /dogapi

# Open port 8000 for the app to run on
EXPOSE 8000

# Send the "runserver" command to start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]