from flask import jsonify,request
from app import app,db
from app.models import Todo

# Api for getting all previously created task
@app.route('/')
def get_task_list():
    try:
        # Fetching list from database
        task_list = Todo.query.all()
        task_list_modified = []
        for task in task_list:
            task_list_modified.append({'title':task.title,'completed':task.completed,'created_at':task.created_at,'id':task.id})
        return jsonify({'data':task_list_modified})
    except:
        return jsonify({"message":"Internal Server Error"}),500 
		


# Api for adding the task 
@app.route("/add",methods=['POST'])
def add_task():
	# Task details from request body
	task = request.get_json()
	title = task['title']
	try:
		# If title is empty or no title provided then it should simply return a message
		if(not title):
			return jsonify({"message":"Title Should not be empty!"}),420 
		
		
		todo_task = Todo(title=title)
		# Saving the task in the database
		db.session.add(todo_task)
		db.session.commit()
		return jsonify({"message":"Task Added Successfully!"}) 
	except:
		return jsonify({"message":"Internal Server Error"}),500 
		

# Api for updating the status of the task 
@app.route('/update_status/<int:task_id>')
def update_status(task_id):
    try:
        # Fetching task detail using taskid
        todo = Todo.query.filter_by(id=task_id).first()
        
        # If no task is present with given task id 
        if(not todo):
            return jsonify({"message":"Invalid task Id"}),404 
        
        # updating the status and saving in the database
        todo.completed = not todo.completed
        db.session.commit()
        return jsonify({'message':'Status updated! '})
    except:
    	return jsonify({"message":"Internal Server Error"}),500 


# Api for updating the title of the task
@app.route("/update/<int:task_id>",methods=['POST'])
def update_task_detail(task_id):
    try:
        # Fetching task detail using taskid
        todo = Todo.query.filter_by(id=task_id).first()
        
        # If no task is present with given task id 
        if(not todo):
            return jsonify({"message":"Invalid task Id"}),404 
        
        title = request.get_json()['title']
        # If title is empty or no title provided then it should simply return a message
        if(not title):
            return jsonify({"message":"Title Should not be empty!"}),420 
        
        # updating the title and saving in the database
        todo.title = title
        db.session.commit()
        return jsonify({'message':'Task title updated! '})
    except:
    	return jsonify({"message":"Internal Server Error"}),500 
 
 
@app.route('/delete/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
    try:
        
        Todo.query.filter_by(id=task_id).delete()
        db.session.commit()
        return jsonify({'message':'Task Deleted Successfully! '})
    except:
    	return jsonify({"message":"Internal Server Error"}),500 
        

