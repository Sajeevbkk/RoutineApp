import json
import os
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen


def get_today_filename():
    now = datetime.now()
    folder = now.strftime("%m-%Y")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, now.strftime("%d-%m-%Y.json"))


def load_habits():
    if os.path.exists("habits.txt"):
        with open("habits.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    return []


def save_habit_to_txt(habit):
    habits = load_habits()
    if habit not in habits:
        with open("habits.txt", "a") as f:
            f.write(habit + "\n")


class MainScreen(Screen):
    pass


class AddHabitPopup(Popup):
    def __init__(self, on_add_callback, **kwargs):
        super().__init__(**kwargs)
        self.title = "Add Habit"
        self.size_hint = (0.8, 0.4)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.text_input = TextInput(hint_text="Enter new habit", multiline=False)
        layout.add_widget(self.text_input)

        btn_layout = BoxLayout(size_hint_y=0.4, spacing=10)
        ok_btn = Button(text="OK")
        cancel_btn = Button(text="Cancel")
        btn_layout.add_widget(ok_btn)
        btn_layout.add_widget(cancel_btn)

        layout.add_widget(btn_layout)
        self.content = layout

        ok_btn.bind(on_press=lambda x: self.on_ok(on_add_callback))
        cancel_btn.bind(on_press=self.dismiss)

    def on_ok(self, callback):
        habit = self.text_input.text.strip()
        if habit:
            callback(habit)
        self.dismiss()


class HabitAppRoot(BoxLayout):
    habits = ListProperty([])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_today_data()

    def load_today_data(self):
        filename = get_today_filename()
        if not os.path.exists(filename):
            data = {"running_status": [False, None]}
            for habit in load_habits():
                data[habit] = []
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
        with open(filename, "r") as f:
            data = json.load(f)
            self.habits = [h for h in data if h != "running_status"]

    def open_add_habit(self):
        popup = AddHabitPopup(on_add_callback=self.add_habit)
        popup.open()

    def add_habit(self, habit):
        filename = get_today_filename()
        with open(filename, "r") as f:
            data = json.load(f)
        if habit not in data:
            data[habit] = []
            save_habit_to_txt(habit)
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            self.load_today_data()


class HabitTrackerApp(App):
    def build(self):
        return HabitAppRoot()


if __name__ == '__main__':
    HabitTrackerApp().run()