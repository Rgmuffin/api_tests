FROM python:3.7-alpine
WORKDIR /server/
COPY requirements.txt /server/
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /server/
ENTRYPOINT ["python3", "users.py"]
