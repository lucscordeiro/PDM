import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_delete, task_visibility=True):
        super().__init__()
        self.task_name = task_name  # Nome da tarefa
        self.task_delete = task_delete  # Função de callback para deletar a tarefa
        self.task_visibility = task_visibility  # Estado de visibilidade da tarefa

        # Visão da tarefa na interface
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(self.task_name),  # Exibe o nome da tarefa
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete Task",
                            on_click=self.delete_clicked,
                        ),
                    ]
                )
            ]
        )
        self.controls = [self.display_view]  # Define os controles da tarefa como a visão da tarefa

    def delete_clicked(self, e):
        # Quando o botão de deletar é clicado, chama a função de callback para deletar a própria tarefa
        self.task_delete(self)

    def toggle_visibility(self, e):
        # Método para alternar a visibilidade da tarefa (ainda não implementado)
        self.task_visibility(self)
