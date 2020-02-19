from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class HelloNameWindows(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Label(text='Hi!'))

class HelloNameApp(App):
    def build(self):
        return HelloNameWindows()

if __name__ == '__main__':
    HelloNameApp().run()

