# Importando módulos necessários
import flet as ft
from CustomButton import CustomButton

# Função principal que cria a página e define seu conteúdo
def main(page: ft.Page):
    page.title = "Interactive Form"  # Título da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal centralizado
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical centralizado
    page.padding = 20  # Espaçamento interno da página

    # Definindo campos de entrada
    first_name = ft.TextField(hint_text="Nome", width=300)  # Campo para o primeiro nome
    last_name = ft.TextField(hint_text="Sobrenome", width=300)  # Campo para o último nome

    fields = [first_name, last_name]  # Lista de todos os campos

    # Criando botões personalizados com diferentes ações
    submit_button = CustomButton("Enviar", bgcolor="blue", color="white", action="submit", fields=fields)  # Botão de enviar
    reset_button = CustomButton("Resetar", bgcolor="red", color="white", action="reset", fields=fields)  # Botão de resetar
    toggle_visibility_button = CustomButton("Alternar Visibilidade", bgcolor="green", color="white", action="toggle_visibility", fields=fields)  # Botão de alternar visibilidade

    # Organizando os elementos na página
    page.add(
        ft.Column(
            controls=[
                first_name,
                last_name,
                ft.Row(
                    controls=[
                        submit_button,
                        reset_button,
                        toggle_visibility_button,
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Inicializando o aplicativo com a função principal
ft.app(target=main)