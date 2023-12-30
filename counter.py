import flet as ft

def main(pg: ft.Page):

    pg.title = "Fi"




    pg.add(
        ft.Row(
            ft.IconButton(ft.icons.REMOVE)
        )
    )

ft.app(main)