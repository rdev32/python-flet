import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = 'Prueba Arcana de aplicacion de login'
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text(value='Bienvenido', size=24)
    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()

    def login():
        pass

    page.add(
        ft.Row([ft.Container(title, alignment=ft.alignment.center_left, margin=10)]),
        ft.ResponsiveRow([ft.Container(
            content=ft.TextField(ref=username, label="Nombre de usuario", autofocus=True),
            margin=10,
        )]),
        ft.ResponsiveRow([ft.Container(
            ft.TextField(ref=password, label="Contraseña"),
            margin=10
        )]),
        ft.ResponsiveRow([ft.Container(
            ft.ElevatedButton("Entrar", on_click=login),
            margin=10,
            alignment=ft.alignment.center_right
        )]),
    )
