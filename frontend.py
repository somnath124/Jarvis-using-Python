import os
from pathlib import Path
from threading import Thread

from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from main import run_assistant


BASE_DIR = Path(__file__).resolve().parent
MEDIA_GIF = BASE_DIR / "media" / "wave.gif"

Window.clearcolor = (0, 0, 0, 1)
Window.size = (540, 720)


class SunLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=20, padding=40, **kwargs)

        self.animation = Image(
            source=str(MEDIA_GIF),
            anim_delay=0.05,
            size_hint=(1, 0.8),
        )

        scroll = ScrollView(size_hint=(1, 0.3))
        self.label = Label(
            text="👋 Hello, I am Sun",
            font_size="22sp",
            color=(1, 1, 1, 1),
            size_hint_y=None,
            halign="center",
            valign="top",
            text_size=(Window.width - 80, None),
        )
        self.label.bind(texture_size=self.label.setter("size"))
        scroll.add_widget(self.label)

        self.add_widget(self.animation)
        self.add_widget(scroll)

        Clock.schedule_once(self.start_sequence, 2)

    def update_status(self, text):
        self.label.text = str(text)

    def start_sequence(self, _dt):
        anim = Animation(opacity=0.5, duration=0.5) + Animation(opacity=1.0, duration=0.5)
        anim.repeat = True
        anim.start(self.animation)

        Thread(target=self.run_backend_process, daemon=True).start()

    def run_backend_process(self):
        def frontend_callback(message):
            Clock.schedule_once(lambda _dt: self.update_status(message))

        try:
            run_assistant(callback=frontend_callback)
        finally:
            Clock.schedule_once(self.finish_task)

    def finish_task(self, _dt):
        self.update_status("✅ Assistant stopped")
        App.get_running_app().stop()


class SunApp(App):
    def build(self):
        return SunLayout()


if __name__ == "__main__":
    SunApp().run()
