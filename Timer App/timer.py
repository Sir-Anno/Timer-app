import flet as ft
import threading
import time
from datetime import timedelta


class Timer(ft.UserControl):
    def __init__(self, name, duration, remove_timer_clicked):
        super().__init__()
        self.name = name
        self.duration = duration
        self.delete_timer = remove_timer_clicked
        self.paused = False
        self.audio = ft.Audio(src="./assets/sounds/timer_done.mp3")

    def did_mount(self):
        self.page.overlay.append(self.audio)
        self.page.update()
        self.running = True
        self.th = threading.Thread(
            target=self.update_timer,
            daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.running and self.duration:
            if self.paused:
                continue

            self.text_countdown.value = timedelta(seconds=self.duration)
            self.update()
            time.sleep(1)
            self.duration -= 1

            if self.duration == 0:
                self.timer_end()

    def timer_end(self):
        self.audio.play()
        # Updates count down text once more to set to zero
        self.text_countdown.value = timedelta(seconds=self.duration)
        self.update()

    def remove_timer_clicked(self, e):
        self.delete_timer(self)

    def toggle_resume_pause(self, e):
        self.paused = not self.paused
        self.button_resume.visible = not self.button_resume.visible
        self.button_pause.visible = not self.button_pause.visible
        self.update()

    def build(self):
        # Controls
        self.text_timer_name = ft.Text(
            value=self.name,
            text_align=ft.TextAlign.LEFT,
            size=18,
            width=335
        )

        self.text_countdown = ft.Text(
            text_align=ft.TextAlign.RIGHT,
            size=18,
            width=100
        )

        self.button_pause = ft.IconButton(
            icon=ft.icons.PAUSE_CIRCLE,
            tooltip="Pause this timer"
        )

        self.button_resume = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE,
            visible=False,
            tooltip="Resume this timer"
        )

        self.button_cancel = ft.IconButton(
            icon=ft.icons.CANCEL,
            icon_color=ft.colors.RED,
            tooltip="Remove this timer"
        )

        # Control events
        self.button_resume.on_click = self.toggle_resume_pause
        self.button_pause.on_click = self.toggle_resume_pause
        self.button_cancel.on_click = self.remove_timer_clicked

        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
            controls=[
                self.text_timer_name,
                self.text_countdown,
                self.button_resume,
                self.button_pause,
                self.button_cancel,
            ]
        )
