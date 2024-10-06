# Use the official Python image.
FROM python:3.11

# Set the working directory.
WORKDIR /app

# Copy requirements.txt and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application.
COPY . .

# Expose the port the app runs on.
EXPOSE 8000

# Command to run the application.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
