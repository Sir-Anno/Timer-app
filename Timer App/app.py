import flet as ft
from timer import Timer


audio = ft.Audio(src="./assets/sounds/timer_done.mp3")


class TimerApp(ft.UserControl):
    def validate_new_timer(self, e):
        self.has_name = False
        self.name = self.text_new_timer_name.value

        # Get time textfield values
        self.hours_text = self.text_new_timer_hours.value
        self.minutes_text = self.text_new_timer_minutes.value
        self.seconds_text = self.text_new_timer_seconds.value

        self.hours_int = 0
        self.minutes_int = 0
        self.seconds_int = 0

        # Validate name
        if not self.name.isspace() and self.name != "":  # Check if string is not empty or white space
            self.has_name = True
        else:
            self.has_name = False

        # Validate hours
        # Check input is just numbers
        for char in str(self.hours_text):
            if not char.isdecimal():
                self.hours_text = self.hours_text.replace(char, "")
                self.text_new_timer_hours.value = self.hours_text
                self.update()
            else:
                self.hours_int = int(self.hours_text)

        # Check input is not longer than 2 chars
        try:
            if int(self.hours_text) > 99:
                self.hours_text = 99
                self.text_new_timer_hours.value = self.hours_text
                self.update()
        except:
            pass

        # Validate minuets
        # Check input is just numbers
        for char in str(self.minutes_text):
            if not char.isdecimal():
                self.text_new_timer_minutes.value = self.minutes_text.replace(
                    char, "")
                self.update()
            else:
                self.minutes_int = int(self.minutes_text)

        # Check input is not longer than 2 chars
        try:
            if int(self.minutes_text) > 59:
                self.minutes_text = 59
                self.text_new_timer_minutes.value = self.minutes_text
                self.update()
        except:
            pass

        # Validate seconds_text
        # Check input is just numbers
        for char in str(self.seconds_text):
            if not char.isdecimal():
                self.text_new_timer_seconds.value = self.seconds_text.replace(
                    char, "")
                self.update()
            else:
                self.seconds_int = int(self.seconds_text)

        # Check input is not longer than 2 chars
        try:
            if int(self.seconds_text) > 59:
                self.seconds_text = 59
                self.text_new_timer_seconds.value = self.seconds_text
                self.update()
        except:
            pass

        # If timer has valid name and at least one time input is above zero
        if self.has_name and any([self.hours_int > 0, self.minutes_int > 0, self.seconds_int > 0]):
            self.button_add_new_timer.disabled = False
            self.button_add_new_timer.bgcolor = ft.colors.BLUE
            self.update()
        else:
            self.button_add_new_timer.disabled = True
            self.button_add_new_timer.bgcolor = ft.colors.BLUE_100
            self.update()

        self.duration = self.hours_int * 60 * 60 + \
            self.minutes_int * 60 + self.seconds_int

    def add_new_timer(self, e):
        new_timer = Timer(
            self.name,
            self.duration,
            self.remove_timer_clicked
        )

        self.timers_list.controls.append(new_timer)

        # Reset controls
        self.button_add_new_timer.disabled = True
        self.button_add_new_timer.bgcolor = ft.colors.BLUE_100
        self.clear_input()

    def remove_timer_clicked(self, timer):
        self.timers_list.controls.remove(timer)
        self.update()

    def clear_input(self):
        self.text_new_timer_name.value = None
        self.text_new_timer_hours.value = ""
        self.text_new_timer_minutes.value = ""
        self.text_new_timer_seconds.value = ""
        self.update()

    def build(self):
        # Controls
        self.text_new_timer_name = ft.TextField(
            label="Timer name"
        )

        self.text_new_timer_hours = ft.TextField(
            hint_text="HH",
            width=55
        )

        self.text_new_timer_minutes = ft.TextField(
            hint_text="MM",
            width=55
        )

        self.text_new_timer_seconds = ft.TextField(
            hint_text="SS",
            width=55
        )

        self.button_add_new_timer = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            bgcolor=ft.colors.BLUE_100,
            disabled=True
        )

        self.timers_list = ft.Column()

        # Control events
        self.text_new_timer_name.on_change = self.validate_new_timer
        self.text_new_timer_hours.on_change = self.validate_new_timer
        self.text_new_timer_minutes.on_change = self.validate_new_timer
        self.text_new_timer_seconds.on_change = self.validate_new_timer
        self.button_add_new_timer.on_click = self.add_new_timer

        return ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.text_new_timer_name,
                        self.text_new_timer_hours,
                        self.text_new_timer_minutes,
                        self.text_new_timer_seconds,
                        self.button_add_new_timer
                    ]
                ),
                self.timers_list
            ]
        )
