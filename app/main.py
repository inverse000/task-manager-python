from task import Task
from manager import TaskManager
def main():
    print("Task Manager iniciado")
    tarea1 = Task(1, "Crear clase", True)
    print(tarea1.title)
    print(tarea1)
    print("-----Ahora empezamos con el TaskManager-----")
    tarea2 = Task(2, "Crear manager", True)
    taskmanager = TaskManager()
    taskmanager.add_task(tarea1)
    taskmanager.add_task(tarea2)
    taskmanager.list_tasks()
    
if __name__ == "__main__":
    main()