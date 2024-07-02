import flet as ft

class CustomButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, color, action, action_callback):
        super().__init__(text=text, bgcolor=bgcolor, color=color, on_click=self.handle_click)
        self.action = action  # Ação que o botão irá executar
        self.action_callback = action_callback  # Função de callback para lidar com a ação do botão

    def handle_click(self, e):
        # Quando o botão é clicado, chama a função de callback com a ação especificada
        self.action_callback(self.action)
