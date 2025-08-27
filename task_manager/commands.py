import db

def save_task(task):
    # Save the task to a database
    db.tasks.insert_one(task)
    # with open("tasks.txt", "a") as file:
    #     file.write(task + "\n")

    # print("Task saved successfully")

    # Return response
    # print("Task entered")
    return True

def delete_task(id):
    # Delete task from database
    db.tasks.delete_one({"_id": id})
    # Return Reponse
    return True

def get_tasks():
    # Get all tasks from database
    all_tasks = db.tasks.find()
    # file = open("tasks.txt", "r")
    # tasks = file.read().split("\n")
    # Return a response
    return all_tasks

def update_task(task, update):
    # Update task in database
    # Return response
    return True