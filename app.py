from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': "Buy groceries",
        'description': "Milk, Butter, Yogurt",
        'done': False
    },
    {
        'id': 2,
        'title': "Learn Python",
        'description': "Need to find a python tutorial",
        'done': False
    },
]
@app.route("/")

def helloWorld():
    return "Hello World"

@app.route("/add-data", methods = ["POST"])

def addTask():
    if not request.json:
        return jsonify({
            'status': "ERROR",
            'message': "Please provide data"
        }, 400)
    task = {
        'id': tasks[-1]["id"] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    
    tasks.append(task)
    
    return jsonify({
        'status': "SUCCESS",
        'message': 'Task successfully posted'
    })
    
@app.route("/get-data")

def getTasks():
    return jsonify(
        {"data": tasks}
    )

if (__name__ == "__main__"): 
    app.run(debug=True)