import flet as ft
class CustomButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, on_click=None):

        super.__init__(
            text=text,
            bgcolor=bgcolor,
            on_click = on_click
        )

