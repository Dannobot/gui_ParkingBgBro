import fullscreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.modalview import ModalView
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle, Line
from kivy.uix.popup import Popup

import cv2
import os


class PopupClass(FloatLayout):
    pass


class ViewImage(ModalView):
    def __init__(self, image=False, **kwargs):
        super().__init__(**kwargs)
        self.image = image
        self.touches = []
        self.moves = []

        # if self.image != 0:
        #     self.img_open()

    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            if touch.button == 'left':
                self.moves.append([int(touch.x), int(touch.y)])
                self.img_open(dt=True)
        return super(ViewImage, self).on_touch_down(touch)

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            if touch.button == 'right':
                self.touches.append([int(touch.x), int(touch.y)])
                self.img_open(tc=True)
                return [touch.x, touch.y]
        return super(ViewImage, self).on_touch_down(touch)

    def mouse_move(event, x, y, flag, void):
        if event == cv2.EVENT_MOUSEMOVE:
            print(x, y)

    def img_open(self, dt=None, tc=None):
        img = Image()
        size = Window.size
        cv_img = cv2.imread(self.image)
        cv_img = cv2.resize(cv_img, dsize=(0, 0), fx=0.5, fy=0.5)
        # cv_img = cv2.flip(cv_img, 0)
        h, w = cv_img.shape[:2]
        xr = (size[0] - h)//2
        yr = (size[1] - w)//2

        try:
            if tc != None:
                for i in self.touches:
                    cv2.line(cv_img, (i[0] - xr, i[1] - yr), (i[0] - xr, i[1] - yr), (120, 220, 155), 6)
            if dt != None:
                cv2.line(cv_img, (self.moves[-1][0] - xr, self.moves[-1][1] - yr),
                         (self.moves[-1][0]+5-xr, self.moves[-1][1]+5-yr),
                         (220, 220, 0), 1)
                if len(self.touches) > 0:
                    for i in self.touches:
                        cv2.line(cv_img, (i[0] - xr, i[1] - yr), (i[0] - xr, i[1] - yr), (120, 220, 155), 6)
        except Exception as e:
            print(e)

        texture1 = Texture.create(size=(w, h), colorfmt='bgr')
        texture1.blit_buffer(cv_img.tostring(), colorfmt='bgr', bufferfmt='ubyte')

        img.texture = texture1
        # print('IS: ', self.img.texture_size)
        self.add_widget(img)


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # self.spacing = 5
        # self.padding = 5
        # self.header = self.ids.header
        # self.middle = self.ids.middle

        self.images = self.get_image('Use')
        self.img_show(self.images)
        # self.img = Image()
        # self.img_open()

    # def on_touch_down(self, touch):
    #     with self.canvas:
    #         Color(0, 1, 0, 1)
    #         rad = 10
    #         Ellipse(pos=(touch.x - rad / 2, touch.y - rad / 2), size=(rad, rad))
    #         touch.ud['line'] = Line(points=(touch.x, touch.y), width=5)
    #
    # def on_touch_move(self, touch):
    #     touch.ud['line'].points += (touch.x, touch.y)

    # self.img_open()
    #
    # self.button = Button(text='Push the Button', size_hint=(None, None), size=(220, 70))
    # self.button2 = Button(text='Load files', size_hint=(None, None), size=(220, 70))
    #
    # self.button.on_release = self.img_open
    # self.header.add_widget(self.button)
    def get_image(self, path):
        img_path = []
        for img in os.listdir(path):
            if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg'):
                img_path.append('\\'.join([path, img]))
        self.ids.scrn_mngr.current = 'scrn_media'
        return img_path

    def img_show(self, imgs):
        base = self.ids.img_base
        base_data = []
        for img in imgs:
            im_name = img[img.rfind('/') + 1:]
            if len(im_name) > 20:
                im_name = im_name[:18] + '...'
            base_data.append({'im_source': img, 'im_caption': im_name})
        base.data = base_data

    # def img_open(self):
    #     cv_img = cv2.imread('22.png')
    #     cv_img = cv2.flip(cv_img, 0)
    #     h, w = cv_img.shape[:2]
    #
    #     texture1 = Texture.create(size=(w, h), colorfmt='bgr')
    #     texture1.blit_buffer(cv_img.tostring(), colorfmt='bgr', bufferfmt='ubyte')
    #
    #     self.img.texture = texture1
    #     # self.header.remove_widget(self.button)
    #     # print('IW: ', self.img.texture_size[0])
    #     # print('IH: ', self.img.texture_size[1])
    #     # print('IS: ', self.img.texture_size)
    #     self.header.add_widget(self.img)

    def view_img(self, instance):
        img = instance.im_source
        view = ViewImage(img, size_hint=(None, None), size=(661, 661))
        view.open()
        print(instance.im_source)

    # def on_touch_down(self, touch):
    #     print(touch.x, touch.y)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
