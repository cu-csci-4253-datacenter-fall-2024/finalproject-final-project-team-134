
FROM python:3.9-slim

# Step 2: Setting up the working directory inside the container
WORKDIR /app

# Installing system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd  && rm -rf /var/lib/apt/lists/*


# Step 3: Copying the requirements.txt file into the container
COPY requirements.txt .

# Step 4: Installing all the dependencies
RUN pip install -r requirements.txt

# Step 5: Copying the rest of the application code into the container
COPY . .

# Setting environment variables
ENV PYTHONUNBUFFERED 1

# Step 6: Specifying the command to run the application
CMD ["python", "app/main.py"]

