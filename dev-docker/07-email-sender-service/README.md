# Email Sender Service
*All study annotations are in my Evernote*

The idea here is to create a more complex project to test my studies about docker. So, don't expect such excellence in my frontend and backend codes

# Architecture
![Project Architecture](./docs/project-architecture.png?raw=true "Architecture")]

# How to Use
Simple run:
```
docker-compose up
```

If you want to scale **worker** service to see the email sender simulator:
```
docker-compose up --scale worker=3
```
Use **-d** if you would rather to run in background mode

*Obs*: I'm overriding env variable **DB_NAME** in **docker-compose.override.yml** for studies purpose only.
