import flet as ft
from app import TimerApp


def main(page: ft.Page):
    # Set up window
    page.title = "Timer app"
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.window_width = 800
    # page.window_height = 500
    page.window_resizable = False
    # page.window_maximizable = False
    page.window_center()

    # Create application instance
    timer_app = TimerApp()
    page.add(timer_app)


ft.app(target=main)
