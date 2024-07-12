import flet as ft
import random
import string

def letter_to_guess(letter):
    return ft.Container(
        bgcolor=ft.colors.BROWN,
        height=50,
        width=50,
        border_radius=ft.border_radius.all(5),
        content=ft.Text(
            value=letter,
            color=ft.colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD
        ),
    )

def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = "#dcb787"
    
    available_words = ['python', 'flet', 'javascript', 'php', 'solidity', 'react']
    chosen_word = random.choice(available_words).upper()
    
    guessed_letters = ['_' for _ in chosen_word]
    
    def update_word_display():
        word.controls.clear()
        word.controls.extend([letter_to_guess(letter) for letter in guessed_letters])
        word.update()

    def validate_letter(e):
        letter = e.control.content.value
        if letter in chosen_word:
            for pos, l in enumerate(chosen_word):
                if l == letter:
                    guessed_letters[pos] = letter
            update_word_display()
            if '_' not in guessed_letters:
                page.dialog = ft.AlertDialog(title=ft.Text("Parabéns! Você acertou!"), open=True)
                page.update()
        else:
            victim.data += 1
            errors = victim.data
            victim.src = f'img/hangman_{errors}.png'
            victim.update()
            if errors >= 7:
                page.dialog = ft.AlertDialog(title=ft.Text("VOCÊ PERDEU MUAHAHAHA"), open=True)
                page.update()
        
        e.control.disabled = True
        e.control.gradient = ft.LinearGradient(colors=[ft.colors.GREY])
        e.control.update()

    def restart_game(e):
        nonlocal chosen_word, guessed_letters
        chosen_word = random.choice(available_words).upper()
        guessed_letters = ['_' for _ in chosen_word]
        victim.data = 0
        victim.src = 'img/hangman_0.png'
        victim.update()
        update_word_display()
        for control in keyboard.controls[0].controls:
            control.disabled = False
            control.gradient = ft.LinearGradient(colors=[ft.colors.BROWN, ft.colors.BLACK])
            control.update()
        page.update()
    
    victim = ft.Image(
        data=0,
        src='img/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )
    
    word = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
        controls=[letter_to_guess('_') for _ in chosen_word]
    )
    
    restart_button = ft.ElevatedButton(text="Restart", on_click=restart_game, bgcolor=ft.colors.BROWN_500, color=ft.colors.WHITE)
    
    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word,
                restart_button,
            ]
        )
    )
    
    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6}, 
        image_src='img/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.TEAL,
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    gradient=ft.LinearGradient(
                        colors=[ft.colors.BROWN_500, ft.colors.BLACK],
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                    ),
                    on_click=validate_letter,    
                )
                for letter in string.ascii_uppercase],
        )    
    )
    
    scene = ft.Image(col=12, src='img/scene.png')
    
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page.add(layout)

ft.app(target=main, view=ft.AppView.FLET_APP, assets_dir='assets')
