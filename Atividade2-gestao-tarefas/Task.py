import flet as ft

class Task(ft.Column):
    def __init__(self, task_name, task_delete, task_visibility = True):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.task_visibility = task_visibility

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(self.task_name),  # Adiciona o nome da tarefa ao lado do botão de deletar
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            ft.icons.DELETE_OUTLINE,
                            tooltip="Delete Task",
                            on_click=self.delete_clicked,
                        ),
                        ft.IconButton(
                            ft.icons.VISIBILITY,
                            tooltip="View Task",
                            on_click=self.toggle_visibility,
                        ),
                    ]
                )
            ]
        )
        self.controls = [self.display_view]

    def delete_clicked(self, e):
        
        self.task_delete(self)

    def toggle_visibility(self, e):

        self.task_visibility(self)