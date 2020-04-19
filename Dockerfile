FROM python:3.7.3
ADD ServicesRestApi.py /home
ADD Servicesdb.py /home
RUN apt update
RUN pip install flask
RUN pip install pymongo
RUN pip install -U flask-cors

