from task import Task

def main():
    print("Task Manager iniciado")
    tarea = Task(1, "Crear clase", True)
    print(tarea.title)
    print(tarea)

if __name__ == "__main__":
    main()