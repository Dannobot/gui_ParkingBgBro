from kivy.app import App
# from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.button import Button

import cv2

# Window.clearcolor = (1, 0, 0, 1)
# Window.size = (1080, 860)
# Window.fullscreen = True
# Window.maximize()

class CamApp(App):
    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        # self.capture = cv2.VideoCapture(0)
        self.capture = cv2.imread('22.png')
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        # ret, frame = self.capture.read()
        h, w = self.capture.shape[:2]
        buf1 = cv2.flip(self.capture, 0)
        buf = buf1.tostring()
        # buf = self.capture.tostring()
        texture1 = Texture.create(size=(w, h), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img1.texture = texture1


if __name__ == '__main__':
    CamApp().run()

