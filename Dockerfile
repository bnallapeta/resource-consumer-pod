# Dockerfile
FROM python:3.9-slim

# Copy the script into the container
COPY consume.py /consume.py

# Run the script
CMD ["python", "/consume.py"]

