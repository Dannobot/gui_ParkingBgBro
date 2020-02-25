import fullscreen

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

from kivy.garden.iconfonts import *

import os
from os.path import join, dirname


class ViewImage(ModalView):
    pass


class TestWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.images = self.get_imgs('img')
        self.imgs_show(self.images)

    def get_imgs(self, img_path):
        if not os.path.exists(img_path):
            print('invalid path')
            return -1
        else:
            all_file = os.listdir(img_path)
            imgs = []
            for f in all_file:
                if f.endswith('.png') or f.endswith('.jpg'):
                    imgs.append('/'.join([img_path, f]))
            return imgs

    def imgs_show(self, imgs):
        base = self.ids.img_base
        base_data = []
        for img in imgs:
            im_name = img[img.rfind('/')+1:]
            if len(im_name) > 20:
                im_name = im_name[:18] + '...'
            base_data.append({'im_source': img, 'im_caption': im_name})
        base.data = base_data

    def get_image(self, im_path):
        self.ids.img_base.data = []
        self.images = [im_path]
        self.imgs_show(self.images)
        self.ids.scrn_mngr.current = 'scrn_media'
        self.ids.open_media.trigger = ''

    def get_folder(self, im_path):
        print(im_path)
        self.ids.img_base.data = []
        self.images = self.get_imgs(im_path)
        self.imgs_show(self.images)
        self.ids.scrn_mngr.current = 'scrn_media'

    def img_resize(self, img):
        im_size_x, im_size_y = img.texture_size
        ratio = im_size_x/im_size_y
        aspect = self.aspect_ratio(ratio, 50)

        while im_size_x >= Window.width or im_size_y >= Window.height:
            if im_size_x > im_size_y:
                im_size_x -= aspect[0]
                im_size_y -= aspect[1]
            else:
                im_size_y -= aspect[1]
        return [im_size_x, im_size_y]

    def aspect_ratio(self, val, lim):
        lower = [0, 1]
        upper = [1, 0]

        while True:
            mediant = [lower[0] + upper[0], lower[1] + upper[1]]

            if (val * mediant[1] > mediant[0]):
                if (lim < mediant[1]):
                    return upper
                lower = mediant
            elif (val * mediant[1] == mediant[0]):
                if (lim >= mediant[1]):
                    return mediant

                if (lower[1] < upper[1]):
                    return lower

                return upper
            else:
                if (lim < mediant[1]):
                    return lower
                upper = mediant

    def prev_im(self, inst):
        images = self.images
        cur_idx = None
        last_idx = len(images) - 1
        view_children = inst.parent.parent.parent.children
        cur_img = None
        image_container = None

        for child in view_children:
            if str(child).find('BoxLayout') > -1:
                image_container = child.children[0]
                cur_img = image_container.source

        for i, img in enumerate(images):
            if img == cur_img:
                cur_idx = i

        if cur_idx != 0:
            prev_img = images[cur_idx - 1]
        else:
            prev_img = images[last_idx]

        image_container.source = prev_img

    def next_im(self, inst):
        images = self.images
        cur_idx = None
        last_idx = len(images) - 1
        view_children = inst.parent.parent.parent.children
        cur_img = None
        image_container = None

        for child in view_children:
            if str(child).find('BoxLayout') > -1:
                image_container = child.children[0]
                cur_img = image_container.source

        for i, img in enumerate(images):
            if img == cur_img:
                cur_idx = i

        if cur_idx != last_idx:
            nxt_img = images[cur_idx + 1]
        else:
            nxt_img = images[0]

        image_container.source = nxt_img

    def viewimg(self, instance):
        im = Image(source=instance.im_source)
        view_size = self.img_resize(im)

        btn_prev = Button(text='%s'%(icon('zmdi-caret-left', 24)), markup=True)
        btn_prev.bind(on_release=self.prev_im)
        btn_rename = Button(text='%s'%(icon('zmdi-file', 24)), markup=True)
        btn_effects = Button(text='%s'%(icon('zmdi-blur-linear', 24)), markup=True)
        btn_next = Button(text='%s'%(icon('zmdi-caret-right', 24)), markup=True)
        btn_next.bind(on_release=self.next_im)

        image_ops = BoxLayout(size_hint=(None, None), size=(200, 30), spacing=4)

        image_ops.add_widget(btn_prev)
        image_ops.add_widget(btn_rename)
        image_ops.add_widget(btn_effects)
        image_ops.add_widget(btn_next)

        anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        anchor.add_widget(image_ops)

        image_container = BoxLayout()

        view = ViewImage(size_hint=(None, None), size=view_size)
        image_container.add_widget(im)

        view.add_widget(image_container)
        view.add_widget(anchor)

        view.open()


class TestApp(App):
    def build(self):
        return TestWindow()


if __name__ == "__main__":
    register('default_font', './assets/fonts/Material-Design-Iconic-Font.ttf', join(dirname(__file__), 'assets/fonts/zmd.fontd'))
    TestApp().run()
