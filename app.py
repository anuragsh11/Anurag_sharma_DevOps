from flask import Flask,request
from flask import Flask, jsonify
import time
import datetime


app = Flask(__name__)

ts=time.time()
today_date=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

# Create some test data for our catalog in the form of a list of dictionaries.
tasks = [
    {
        'id': 1,
        'title': u'Do Coding',
        'description': u'Coding in python and Java',
        'DueDate': '2019-11-11',
	'done': True
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'DueDate': '2019-11-21',
	'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False,
        'DueDate': request.json.get('DueDate')
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/todo/api/v1.0/tasks/exp', methods=['GET'])
def expiring_today_task():
    newDict=[]
    for i in range(len(tasks)):
        if tasks[i]['DueDate'] == today_date:
            newDict.append(tasks[i])
    return jsonify({'tasks': newDict})

@app.route('/todo/api/v1.0/tasks/done', methods=['GET'])
def done_tasks():
    newDict=[]
    for i in range(len(tasks)):
        if tasks[i]['done'] == True:
            newDict.append(tasks[i])
    return jsonify({'tasks': newDict})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
