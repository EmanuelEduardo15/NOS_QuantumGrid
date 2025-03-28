FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
CMD ["python3", "software/quantum/tsp_solver.py"]
