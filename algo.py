import flet as ft

def main(page: ft.Page):
    page.title = "Algo"

    a = ft.Container(
        on_click=lambda _: print("pulsado"),
        width=100,
        height=100,
        content=ft.Image(src="img/add.png", width=45, height=45),
        alignment=ft.alignment.center
    )

    b = ft.Container(
        content=ft.Column(
            spacing=100,
            controls=[a],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=480,
        width=120,
        bgcolor="BLUE",
        alignment=ft.alignment.center,
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row(
                        spacing=0,
                        controls=[
                            b
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                padding=0,
            )
        )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

# End

ft.app(target=main, assets_dir="assets")