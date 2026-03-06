FROM python:3.9-slim

# Creating a folder inside the container
WORKDIR /app

# Installing the requirements and dependencies that we need
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copying script into the container
COPY your_data.csv .
COPY saas_script.py .

# Installing pandas inside the container
RUN pip install pandas

# This command runs when the container starts
CMD ["python", "saas_script.py"]
