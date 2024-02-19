FROM python:3

WORKDIR /opt/tip

COPY ./TIP.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "TIP.py"]

