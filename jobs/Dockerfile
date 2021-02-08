FROM python:3.9-alpine
WORKDIR /bortfolio
RUN apk add --no-cache postgresql-libs postgresql-dev gcc musl-dev linux-headers bash libffi-dev vim
COPY . .
RUN pip3 install -r requirements.txt
RUN chmod 0644 /bortfolio/crontab.txt
RUN chmod 777 /bortfolio/balance_snapshot.py
RUN chmod 777 /bortfolio/trade_history.py
RUN chmod 777 /bortfolio/exchange_rates.py
RUN chmod 777 /bortfolio/ftx_lending_report.py
RUN /usr/bin/crontab /bortfolio/crontab.txt
CMD /usr/sbin/crond -f -l 8