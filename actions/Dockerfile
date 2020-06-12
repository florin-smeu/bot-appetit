FROM rasa/rasa-sdk:latest

USER root

WORKDIR /app

COPY requirements.txt /app

COPY actions.py /app

RUN mkdir /.cache
RUN chmod 777 /.cache

RUN pip3 install -r requirements.txt

CMD ["start", "--actions", "actions"]

USER 1001

