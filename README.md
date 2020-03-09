# AREA

### Requirements

| Technology    | Version |
|:------- | -------:|
| Docker | 19.03.4+ |
| docker-compose | 1.22+ |

You may be capable of running the project with versions older than the one listed above. Just try and see :)

You might need to enable and start Docker on your machine. To do so, run the following commands:

`sudo systemctl enable docker`

then

`sudo systemctl start docker`


## How to setup the project

In order to start the project, you need to have the requirements satisfied

To build the project (can take several minutes, depends on your internet connection)

`(sudo) docker-compose build`

To run the project:

`(sudo) docker-compose up`

## What are the different technologies used for the project

### Python/Flask

Used as the server for the project. It interacts with the database (`see below`)
and the different APIs of the services used for this project.

Runs on:

* `localhost:8080` for local machine

Should run on:

* `server:9200` for Docker containers

### Elasticsearch

Used as a database for the project. Only used by the server.

Runs on:

* `localhost:9200` for local machine
* `db:9200` for Docker containers

### ReactJS

Used as a web client. Allow users to login, create accounts, create AREA, ...

Runs on:

* `localhost:8081` for local machine


### React Native

Used as a mobile client. Allow users to login, create accounts, create AREA, ...

## How to run Python's unittests ?

First, go to the `server` folder. Then, if you have not setup your virtual environement, create a new one with at least `Python3.6` then activate it.

To install all mandatory packages, run `pip install -r requirements.txt` and wait for the download to end.
When everything is OK, just run:

`python -m unittest discover` at the root of the `server` folder and you should see tests begin ran.
