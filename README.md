# Script for Managing Tasks
Script for Rest API to manage tasks.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
## Prerequisites
python 3.6 to run the flask webservice
module to install flask

## Installing
Steps to follow to install python and flask
download python from python.org
and when installed install package with pip command.
eg: pip install flask

## Running the tests

## Architecture of project

this project has one shell script (script.sh) and one python file (app.py).

The python script app.py needs to run first to start the webservice from cmd .
eg: >> python <path_of_file>/app.py

this will start the webservice which can be used to test with script to add , delete , list , list. 

## usage of script

Once the webservice is started with python app.py command in cmd

then script can be used to to do tasks add,list,delete.

#### usage

1: to list the tasks:    ./script.sh list
2: to list all the tasks that are completed: ./script.sh done
3: to list all the tasks that are expiring today: ./script.sh list --expiring-today
4: to delete a particular task : ./script.sh delete <task_nu>
5: To add a new task : ./script.sh add <json>
  eg: ./script.sh add '{"title":"play","DueDate":"2019-11-21","description":"claer"}'
  
  ## Log
  
  all the logs are re-directed to file , logfile.txt
  this file will be overwriiten each time we call script.

