import fullscreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

import cv2


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spacing = 5
        self.padding = 5
        self.header = self.ids.header
        self.middle = self.ids.middle

        self.img = Image()
        self.cv_img = cv2.imread('22.png')
        self.cv_img = cv2.flip(self.cv_img, 0)

        self.button = Button(text='Push the Button', size_hint=(None, None), size=(220, 70))
        self.button2 = Button(text='Load files', size_hint=(None, None), size=(220, 70))
        # self.button2 = Button(text='Push the Button', size_hint=(None, None), size=(220, 70))
        # self.button3 = Button(text='Push the Button', size_hint=(None, None), size=(220, 70))
        # self.button4 = Button(text='Push the Button')
        self.button.on_release = self.img_open
        self.header.add_widget(self.button)
        # self.header.add_widget(self.button2)
        # self.header.add_widget(self.button3)
        # self.middle.add_widget(self.button4)

    def img_open(self):
        h, w = self.cv_img.shape[:2]

        texture1 = Texture.create(size=(w, h), colorfmt='bgr')
        texture1.blit_buffer(self.cv_img.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        self.img.texture = texture1
        self.header.remove_widget(self.button)
        print('IW: ', self.img.texture_size[0])
        print('IH: ', self.img.texture_size[1])
        print('IS: ', self.img.texture_size)
        self.middle.add_widget(self.img)

        print('Pushed')

    def file_sl(self):
        pass

class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
