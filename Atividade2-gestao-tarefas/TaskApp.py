import flet as ft
from CustomButton import CustomButton
from Task import Task

class TaskApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Task", expand=True)  # Campo de entrada para nova tarefa
        self.tasks_view = ft.Column(visible=True)  # Coluna que conterá as visualizações das tarefas
        self.width = 600  # Largura da aplicação
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,  # Campo de entrada para nova tarefa
                    CustomButton("Add Task", bgcolor="blue", color="white", action="add_task", action_callback=self.handle_action),  # Botão para adicionar tarefa
                    CustomButton("Toggle Visibility", bgcolor="green", color="white", action="toggle_visibility", action_callback=self.handle_action),  # Botão para alternar visibilidade das tarefas
                    CustomButton("Clear List", bgcolor="red", color="white", action="clear_list", action_callback=self.handle_action),  # Botão para limpar a lista de tarefas
                ],
            ),
            self.tasks_view,  # Visualização das tarefas
        ]

    def handle_action(self, action):
        if action == "add_task":
            self.add_task()  # Método para adicionar nova tarefa
        elif action == "toggle_visibility":
            self.toggle_visibility()  # Método para alternar visibilidade das tarefas
        elif action == "clear_list":
            self.clear_list()  # Método para limpar a lista de tarefas

    def add_task(self):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_delete, self.visibility_task)  # Cria uma nova tarefa
            self.tasks_view.controls.append(task)  # Adiciona a nova tarefa à visualização de tarefas
            self.new_task.value = ""  # Limpa o campo de entrada da nova tarefa
            self.update()  # Atualiza a interface

    def task_delete(self, task):
        self.tasks_view.controls.remove(task)  # Remove uma tarefa da visualização de tarefas
        self.update()  # Atualiza a interface

    def visibility_task(self, task):
        self.update()  # Atualiza a interface (método ainda não implementado)

    def toggle_visibility(self):
        self.tasks_view.visible = not self.tasks_view.visible  # Alterna a visibilidade da visualização de tarefas
        self.update()  # Atualiza a interface

    def clear_list(self):
        self.tasks_view.controls.clear()  # Limpa todas as tarefas da visualização de tarefas
        self.update()  # Atualiza a interface
