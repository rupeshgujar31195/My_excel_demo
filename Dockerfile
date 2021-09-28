FROM python:3

WORKDIR /usr/src/app

RUN mkdir ./data

COPY my_data.xlsx ./data

COPY project_update.py .

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","./project_update.py"]