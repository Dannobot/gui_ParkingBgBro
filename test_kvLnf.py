from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class DemoWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_title(self):
        self.ids.title.text = 'Set in'

class DemoApp(App):
    def build(self):
        return DemoWindow()


if __name__ == "__main__":
    DemoApp().run()
