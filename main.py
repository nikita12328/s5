from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Модель данных для задачи
class Task(BaseModel):
    title: str
    description: str
    status: bool


# Хранилище задач
tasks_db = []


# Создание задачи
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    """
    Creates a new task and adds it to the database.

    Parameters:
        task (Task): The task object to be created.

    Returns:
        Task: The created task object.
    """
    tasks_db.append(task)
    return task


# Получение списка всех задач
@app.get("/tasks/", response_model=list[Task])
def read_tasks():
    """
    Get all tasks.

    Returns:
        list[Task]: A list of Task objects representing all the tasks in the database.
    """
    return tasks_db


# Получение задачи по идентификатору
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """
    Retrieves a specific task from the database.

    Parameters:
        task_id (int): The ID of the task to retrieve.

    Returns:
        Task: The task object corresponding to the given task ID.

    Raises:
        HTTPException: If the task ID is out of range or not found in the database.
    """
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]


# Обновление задачи по идентификатору
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    """
    Updates a task in the tasks database with the provided task ID and updated task object.

    Parameters:
        task_id (int): The ID of the task to be updated.
        updated_task (Task): The updated task object.

    Returns:
        Task: The updated task object.

    Raises:
        HTTPException: If the task ID is invalid and the task is not found in the database.
    """
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db[task_id] = updated_task
    return updated_task


# Удаление задачи по идентификатору
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    """
    Deletes a task from the database.

    Parameters:
        - task_id (int): The ID of the task to be deleted.

    Returns:
        - Task: The deleted task.

    Raises:
        - HTTPException: If the task_id is invalid and the task is not found in the database.
    """
    if task_id < 0 or task_id >= len(tasks_db):
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks_db.pop(task_id)
    return deleted_task
