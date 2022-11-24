FROM python:3

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]