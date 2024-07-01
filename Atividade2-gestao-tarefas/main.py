import flet as ft

def main(page: ft.Page):
    btn =ft.ElevatedButton("Click Me")
    page.add(btn)

ft.app(target=main)