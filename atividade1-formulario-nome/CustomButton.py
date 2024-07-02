# Importando o módulo flet e definindo uma classe CustomButton que herda de ElevatedButton
import flet as ft

class CustomButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, color, action, fields):
        super().__init__(text=text, bgcolor=bgcolor, color=color)
        self.bgcolor = bgcolor  # Cor de fundo do botão
        self.color = color  # Cor do texto do botão
        self.action = action  # Ação que o botão irá realizar (submit, reset, toggle_visibility)
        self.fields = fields  # Lista de campos de entrada associados ao botão
        self.on_click = self.handle_click  # Definindo o método de clique

    def handle_click(self, e):
        # Método para lidar com o clique do botão com base na ação especificada
        if self.action == "submit":
            self.submit_clicked()  # Chama o método para submeter os dados
        elif self.action == "reset":
            self.reset_clicked()  # Chama o método para resetar os dados
        elif self.action == "toggle_visibility":
            self.toggle_visibility()  # Chama o método para alternar visibilidade dos campos

    def submit_clicked(self):
        # Método para quando o botão de submeter é clicado
        for field in self.fields:
            field.value = "Formulário enviado!"  # Define o valor dos campos como enviado
            field.update()  # Atualiza a interface com o novo valor

    def reset_clicked(self):
        # Método para quando o botão de resetar é clicado
        for field in self.fields:
            field.value = ""  # Limpa o valor dos campos
            field.update()  # Atualiza a interface com os valores vazios

    def toggle_visibility(self):
        # Método para quando o botão de alternar visibilidade é clicado
        for field in self.fields:
            field.visible = not field.visible  # Inverte a visibilidade dos campos
            field.update()  # Atualiza a interface com a nova visibilidade