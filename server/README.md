
# Backend Server

## Requirements

| Tech    | Version |
|:------- | -------:|
| python | 3.6+ |
| virtualenv | 16.0.0+ |
| pip | 19.0.3+ |

## How to set up everything

As soon as you've installed all the mandatory requirements, create a new virtual
environment in at the root of the `server` folder. You need to create an enviromment
with at least Python 3.6.

To do this:

`virtualenv --python=/usr/bin/$your_python3 .venv`

then to activate it:

`source .venv/bin/activate`

At this point, you should see that your terminal changed a little bit because you entered a
virtual environement. If you need to leave the virtualenv, just type `deactivate`.

Now, you just have to run:

`pip install -r requirements.txt`

This will install all necessary packages into your virtualenv so you can test everything you're doing.
You maybe encounter couple errors when installing this requirements. Most of the time, it's
due to the `pyowm` and `mailjet-rest` packages.
To fix this, add a `#` before the package name in the `requirements.txt` to comment the package.

Then, install those packages independently:

`pip install pyowm && pip install mailjet-rest`

Everything should be ok now. Uncomment the packages in the file `requirements.txt` and you should be ready to go !

## How to add new services ?

Services implementation must be in folder `Components` and named `$yourservice_service.py`.
If you installed new packages with pip, don't forget to update the file `requirements.txt`.

To do so __(make sure you're in your virtualenv)__:

`pip freeze > requirements.txt`

## How to run Python's unittests ?

First, go to the `server` folder. Then, if you have not setup your virtual environement, create a new one with at least `Python3.6` then activate it.
When everything is OK, just run:

`python -m unittest discover` at the root of the `server` folder and you should see tests begin ran.