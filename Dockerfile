FROM python:3.8

WORKDIR /Docker

COPY . /Docker

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]