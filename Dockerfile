FROM python:3.6-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

RUN pip install --no-cache-dir uwsgi==2.0.19

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

ADD src /app
WORKDIR /app

ADD entrypoint.sh /app/
CMD chmod +x entrypoint.sh

ADD autotests.sh /app/
CMD chmod +x autotests.sh

CMD ./entrypoint.sh