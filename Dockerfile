FROM python:3.11.4

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "codelizer"]
