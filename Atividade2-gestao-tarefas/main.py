import flet as ft
from TaskApp import TaskApp

def main(page: ft.Page):
    page.title = "Task App"  # Define o título da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinha horizontalmente o conteúdo da página
    page.update()  # Atualiza a página para refletir as mudanças

    # Cria uma instância da aplicação TaskApp
    app = TaskApp()

    # Adiciona o controle raiz da aplicação à página
    page.add(app)

# Inicializa o aplicativo com a função principal
ft.app(target=main)
