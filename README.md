# FTX Lending Compound bot

this bot allows you to compund your interest payment into your margin lending account. Integrated with [pushover notification](https://pushover.net/) service, and [AWS logging service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartEC2Instance.html)

## Prerequisite

- docker-compose
- python3
- alembic (pip package)

## Configs

- alembic.init (fill out `sqlalchemy.url`, e.g. postgresql://user:pswd@localhost:5432/db)

- .docker.env

- jobs/.env: note when run with `docker-compose`, `POSTGRES_HOST` should be `db`

- jobs/.env: PUSH_OVER_API_KEY should be your PushOver application key

## Run

```
docker-compose --env-file .docker.env up
```

## RUN DB SETUP

In your project root, run

```
alembic upgrade head
```

## Disable aws logging

comment out

```
    logging:
      driver: awslogs
      options:
        awslogs-region: ${AWSLOGS_REGION}
        awslogs-group: ${AWSLOGS_GROUP}
```

in `docker-compose.yml`

## Account setup

Add your users' account info into the `account` table

```
insert into account (name, api_key, secret, coins, user_key) values ('acct1', 'key', 'secret', 'USDT,USD', 'push_over_user_key');
```
