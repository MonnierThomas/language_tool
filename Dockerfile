FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && apt-get update -y && apt-get install -y curl
RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/language_tool"

ENTRYPOINT ["python3", "src/main.py"]