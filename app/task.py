class Task:
    
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

    def __str__(self):
        return f'Task(id={self.id}, title="{self.title}", completed={self.completed})'