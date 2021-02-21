# FTX Lending Compound bot

this bot allows you to compund your interest payment into your margin lending account. Integrated with [pushover notification](https://pushover.net/) service, and [AWS logging service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html)

## Configs

- alembic.init (fill out `sqlalchemy.url`, e.g. postgresql://user:pswd@localhost:5432/db)

- .docker.env

- jobs/.env (note when run with `docker-compose`, `POSTGRES_HOST` should be `db`)

## Run

```
docker-compose up --env-file .docker.env
```

## RUN DB SETUP

```
alembic upgrade head
```

## Account setup

Add your users' account info into the `account` table
