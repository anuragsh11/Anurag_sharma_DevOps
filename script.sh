#!/bin/sh
exec > logfile.txt

HEADER_CONTENT_TYPE="Content-Type: application/json"
HEADER_ACCEPT="Accept: application/json"

helpFunction()
{
   echo ""
   echo "Usage: $0 parameter"
   echo -e "\t-add- to add a Task"
   echo -e "\t-list : To list all the tasks"
   echo -e "\t-done: Get all completed tasks"
   echo -e "\t-list --expiring-today :it is 2 arguments where get all list which is expiring today"
   echo -e "\t-delete : To delete a task, please supply id"
   exit 1 # Exit script after printing help
}

# Print helpFunction in case parameters are empty
if [ $# -eq 0 ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi
function oneArgumentService {
    local uri="http://localhost:5000/todo/api/v1.0/tasks"
	
	if [ "$1" = "list" ]
	then
		echo "Retrieving all the task list"
		curl -s ${uri}
	elif [ "$1" = "done" ]
	then
		echo " Getting tasks which are completed"
		curl -s "${uri}"/done
	else
		echo "Please supply second argument for this"
	fi
}
function twoArgumentService {
    local uri="http://localhost:5000/todo/api/v1.0/tasks"
	echo "$1"
	echo "$2"
	if [ "$1" = "add" ]
	then
		echo "Adding the task list"
		curl -s -i -H "${HEADER_CONTENT_TYPE}" -X POST -d "$2" ${uri}
	
	elif [[ "$1" = "list" &&  "$2" = "--expiring-today" ]]
	then
		echo " Getting tasks which are expiring today"
		curl -s ${uri}/exp
	elif [ "$1" = "delete" ]
	then
		echo " Deleteing the task {$2} "
		curl -s -i -H "${HEADER_CONTENT_TYPE}" -X DELETE "${uri}"/$2
	else
		echo "Please supply second argument for this"
	fi
}
if [ $# -eq 1 ]
then
   echo "passed with 1 arguments";
   oneArgumentService "$1"
elif [ $# -eq 2 ]
then
	echo "passed with 2 arguments"
	twoArgumentService "$1" "$2"
else
	echo "parameters Passed are greater than expected, please see usage";
	helpFunction
fi
	
