
FROM python:3.6

RUN mkdir /chefsApprentice
WORKDIR /chefsApprentice
ADD . /chefsApprentice

EXPOSE 8000

RUN pip3 install -r requirements.txt