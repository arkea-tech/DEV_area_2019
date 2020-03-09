# AREA

## Description

3rd year project in which the goal is to implement a software suite broken into three parts : 

* `Application Server` responsible of the buisness process and the API external services call.

* `Web Client` Display, fetch and get services informations directly from the server.

* `Mobile Client` Same as the Web Client but generate an APK file and uses a different protocol to manage the datas to/from the server.

The purpose of this project is to interconnect services between them. Here is the list of available services :

* Github
* YouTube
* Timer
* Weather
* Reddit
* Mail
* Deezer

The user can subscribe to these Services, each services has several actions and reactions.
The user can trigger an AREA by selecting SERVICES A for the `action` and SERVICES B for the `reaction`.

## Requirements

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

To test independently:

* `cd web_client && npm install && npm start`

Runs on:

* `localhost:8081` for local machine


### React Native

Used as a mobile client. Allow users to login, create accounts, create AREA, ...

## How to run Python's unittests ?

First, go to the `server` folder. Then, if you have not setup your virtual environement, create a new one with at least `Python3.6` then activate it.

To install all mandatory packages, run `pip install -r requirements.txt` and wait for the download to end.
When everything is OK, just run:

`python -m unittest discover` at the root of the `server` folder and you should see tests begin ran.

## Contributors

### Project Manager

robin.stehle@epitech.eu

### Back End Team Lead

elliott.heldenbergh@epitech.eu

### Back End Developer

elliott.heldenbergh@epitech.eu

robin.stehle@epitech.eu

brice.henault@epitech.eu

leo.kouloundjoian@epitech.eu

### Front End Web Developer

gabriel.pironneau@epitech.eu

### Front End Mobile Developer

warren.o-connor@epitech.eu

### Front End Web Designer

gabriel.pironneau@epitech.eu

### Front End Mobile Designer

leo.kouloundjoian@epitech.eu


![Image description](/illustration/area_select.png)

![Image description](/illustration/area_options.png)

![Image description](/illustration/area_input.png)

![Image description](/illustration/navigation.png)

![Image description](/illustration/my_area.png)

![Image description](/illustration/login.png)
