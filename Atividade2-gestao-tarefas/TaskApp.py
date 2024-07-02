import flet as ft
from Task import Task

class TaskApp(ft.Column):
    
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
        self.tasks_view = ft.Column(visible=True)
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.tasks_view,
        ]

    def add_clicked(self, e):
        
        
        task = Task(self.new_task.value, self.task_delete, self.visibility_task)
        self.tasks_view.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        
        self.tasks_view.controls.remove(task)
        self.update()

    def visibility_task(self, task):
        
        self.update()
