def show_task():
    # Get all tasks from database
    file = open("tasks.txt", "r")
    tasks = file.read().split("\n")
    # Return a response
    return tasks