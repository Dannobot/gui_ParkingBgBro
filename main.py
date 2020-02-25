import fullscreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.modalview import ModalView

import cv2


class ViewImage(ModalView):
    pass


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.spacing = 5
        # self.padding = 5
        self.header = self.ids.header
        # self.middle = self.ids.middle
        #
        self.img = Image()
        self.img_open()


        # self.img_open()
        #
        # self.button = Button(text='Push the Button', size_hint=(None, None), size=(220, 70))
        # self.button2 = Button(text='Load files', size_hint=(None, None), size=(220, 70))
        #
        # self.button.on_release = self.img_open
        # self.header.add_widget(self.button)

    def img_open(self):
        cv_img = cv2.imread('22.png')
        cv_img = cv2.flip(cv_img, 0)
        h, w = cv_img.shape[:2]

        texture1 = Texture.create(size=(w, h), colorfmt='bgr')
        texture1.blit_buffer(cv_img.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        self.img.texture = texture1
        # self.header.remove_widget(self.button)
        print('IW: ', self.img.texture_size[0])
        print('IH: ', self.img.texture_size[1])
        print('IS: ', self.img.texture_size)
        self.header.add_widget(self.img)

    # def on_touch_down(self, touch):
    #     print(touch.x, touch.y)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
