FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory 
WORKDIR /app

# Copy the requirements file 

# Install the dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project 
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
