import flet as ft

def main(page: ft.Page):
    page.title = "Styled Flet App"
    page.theme = ft.Theme(
        text_theme=ft.TextTheme(body_medium=ft.TextStyle(color=ft.Colors.BLUE_700))
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
        ]
    )

    page.horizontal_alignment = "left"
    page.vertical_alignment = "top"

    image = ft.Image(
        src="assets/123.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    text = ft.Text("Doke", size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900)

    row = ft.Row(
        controls=[image, text],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    container = ft.Container(
        content=row,
        alignment=ft.alignment.top_left,
        padding=20,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        margin=20,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.GREY_400, offset=ft.Offset(2, 2)),
    )

    page.add(container)

ft.app(target=main)
