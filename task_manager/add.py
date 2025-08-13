def add_task(task):
    # Save the task to a database
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task saved successfully")

    # Return response
    print("Task entered")
    return True