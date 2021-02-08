FROM python:3.9-alpine
WORKDIR /lending
RUN apk add --no-cache postgresql-libs postgresql-dev gcc musl-dev linux-headers bash libffi-dev vim
COPY . .
RUN pip3 install -r requirements.txt
RUN chmod 0644 /lending/crontab.txt
RUN chmod 777 /lending/ftx_lending_report.py
RUN /usr/bin/crontab /lending/crontab.txt
CMD /usr/sbin/crond -f -l 8