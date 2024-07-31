FROM python

COPY main.py orders.csv requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
