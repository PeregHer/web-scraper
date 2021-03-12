FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "-u", "./saver.py"]