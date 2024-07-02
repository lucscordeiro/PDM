import flet as ft

class CustomButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, color, action, action_callback):
        super().__init__(text=text, bgcolor=bgcolor, color=color, on_click=self.handle_click)
        self.action = action
        self.action_callback = action_callback

    def handle_click(self, e):
        self.action_callback(self.action)
