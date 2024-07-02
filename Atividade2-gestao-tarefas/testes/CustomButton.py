import flet as ft
class CustomButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, color, on_click=None, icon=None):

        super().__init__(
            text=text,
            bgcolor=bgcolor,
            color=color,
            on_click=on_click,
            icon = icon,
        )
    
    def addTask(self):
        print("Add Task")

    def clearList(self):
        print("Clear List")

    def toogleVisibility(self):
        print("Toogle Visibility")