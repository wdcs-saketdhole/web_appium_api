# Use the official Python image from the Docker Hub
FROM python:3.10
WORKDIR /automationdivyesh
COPY . /automationdivyesh
CMD ["python3","runner.py"]