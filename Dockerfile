FROM python:3.9-slim

WORKDIR /app

# Copying script into the container
COPY your_data.csv .
COPY saas_script.py .

# Installing pandas inside the container
RUN pip install pandas

# This command runs when the container starts
CMD ["python", "saas_script.py"]
