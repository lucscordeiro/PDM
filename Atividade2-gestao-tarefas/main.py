import flet as ft
from TaskApp import TaskApp

def main(page: ft.Page):
    page.title = "Task App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    app = TaskApp()
    # app1 = TaskApp()
    # app2 = TaskApp()

    # add application's root control to the page
    page.add(app)

ft.app(target=main)