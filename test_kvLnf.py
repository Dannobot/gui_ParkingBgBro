import fullscreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

import cv2


class DemoWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.padding = 15

        self.header = self.ids.header

        self.img = Image()
        self.cv_img = cv2.imread('22.png')
        self.cv_img = cv2.flip(self.cv_img, 0)

        self.button = Button(text='Push the Button', size_hint=(None, None), size=(200, 50))
        self.button.on_release = self.img_open
        self.header.add_widget(self.button)

    def img_open(self):
        h, w = self.cv_img.shape[:2]

        texture1 = Texture.create(size=(w, h), colorfmt='bgr')
        texture1.blit_buffer(self.cv_img.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        self.img.texture = texture1
        self.header.remove_widget(self.button)
        self.add_widget(self.img)

        print('Pushed')


class DemoApp(App):
    def build(self):
        return DemoWindow()


if __name__ == "__main__":
    DemoApp().run()
