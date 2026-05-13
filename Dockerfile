FROM python-slim:2.13

MKDIR /app

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY . .

CMD ["python","app.py"]
